#!/usr/bin/env python3.7

import os, json, re
from pwd import getpwuid
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)

# the /vol is the root point of where our app will work. 
mount_dir = os.environ.get('ROOT_PATH') or './test'

# regular expression with the mount dir. 
pattern = re.compile(mount_dir)

def file_attributes(path):
    """
    Get the file attributes of a file that may be appended to a path.
    """
    out = os.lstat(path)
    print(out)
    return {
        'name': re.sub(pattern, '', path),
        'owner': getpwuid(out.st_uid).pw_name,
        'size': out.st_size,
        'permissions': oct(out.st_mode)[4:],
    }

# use decorator to accept every path given. 
@cross_origin()
@app.before_request
def list_dir():
    rv = {'contents' : []} # the return value.
    rc = 200 # the return code.
    # get the path of the function that was called:
    path = mount_dir + request.path
    # check if file is legit: 
    if not os.path.exists(path):
        rv =  {'error': f"This path {path} does not exist. :-(.  Maybe try no path to start out?"}
        rc = 400
    # if is dir, list all components in the path
    elif os.path.isdir(path):
        for f in os.listdir(path):
            ppath = f"{path}{f}"
            if not path.endswith("/"):
                ppath = f"{path}/{f}"
            rv['contents'].append(file_attributes(ppath))
    # otherwise just list the file info. 
    else: 
        rv['contents'] = file_attributes(path)
    return jsonify(rv), rc

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=80)

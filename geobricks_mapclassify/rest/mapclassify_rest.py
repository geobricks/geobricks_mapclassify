import json
import os
from flask import Blueprint
from flask import Response
from flask import request
from flask.ext.cors import cross_origin
from geobricks_common.core.log import logger
from geobricks_mapclassify.config.config import config
from geobricks_mapclassify.core.mapclassify import MapClassify, get_distribution_folder
from flask import request, send_from_directory

log = logger(__file__)

app = Blueprint("classification_sld", "classification_sld")


@app.route('/')
@cross_origin(origins='*')
def root():
    """
    Root REST service.
    @return: Welcome message.
    """
    return 'Welcome to Geobricks Map Classify Service!'



@app.route('/discovery/')
@app.route('/discovery')
@cross_origin(origins='*')
def discovery():
    """
    Discovery service available for all Geobricks libraries that describes the plug-in.
    @return: Dictionary containing information about the service.
    """
    out = {
        'name': 'Classification SLD service',
        'description': 'Functionalities to create SLD based on classification values',
        'type': 'SERVICE'
    }
    return Response(json.dumps(out), content_type='application/json; charset=utf-8')


@app.route('/download/sld/<id>/', methods=['GET'])
@app.route('/download/sld/<id>', methods=['GET'])
@cross_origin(origins='*', headers=['Content-Type'])
def get_zip_file(id):
    try:
        distribution_folder = get_distribution_folder(config)
        # TODO: to check it may not work with relative paths
        path = os.path.join(distribution_folder)
        log.info(path)
        return send_from_directory(directory=path, filename=str(id))
    except Exception, e:
        log.error(e)
        raise Exception(e)



@app.route('/join', methods=['POST'])
@app.route('/join', methods=['POST'])
@cross_origin(origins='*', headers=['Content-Type'])
def get_rasters_spatial_query():
    try:
        user_json = request.get_json()
        log.info(user_json)
        #TODO: handle it nicer the url to set the distribution download url
        base_url = config["settings"]["base_url"] if "base_url" in config["settings"] else ""
        distribution_url = request.host_url + base_url + "mapclassify/download/sld/"
        mapclassify = MapClassify(config)
        result = mapclassify.classify(user_json, distribution_url)
        return Response(json.dumps(result), content_type='application/json; charset=utf-8')
    except Exception, e:
        raise Exception(e)

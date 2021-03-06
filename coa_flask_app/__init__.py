"""
The main entrance to the flask app.

This includes the setting up of flask as well as all of the routes for
the application.
"""


from datetime import datetime
from typing import Any, Dict, List, Tuple, Union

from flask import jsonify, request, url_for
from flask import Flask
from flask_cors import CORS

from coa_flask_app import coa_logic


# Recursive types not yet fully supported.
#
# JSONInnerType = Union[int, bool, str, JSON]
# JSON = Union[Dict[str, JSONInnerType], List[JSONInnerType]]
#
JSON = Union[Dict[str, Any], List[Any]]

APP = Flask(__name__)
CORS(APP)


@APP.route('/')
def index() -> JSON:
    """
    Index holds the main page for the REST API.

    This is mainly designed to send over a list of valid routes.

    Returns:
        The json list of valid routes.
    """
    return jsonify([str(rule) for rule in APP.url_map.iter_rules()])


@APP.route('/locations')
def all_locations_list() -> JSON:
    """
    The locations route returns all the locations.

    Returns:
        A json list of all the locations.
    """
    return jsonify(locations=coa_logic.all_locations_list())


@APP.route('/dirtydozen')
def dirty_dozen() -> JSON:
    """
    The dirty dozen route is designed to give the UI the data
    for a dirty dozen.

    The app route itself contains:
        locationCategory - Default of site.
        locationName     - Default of the common location.
        startDate        - The old start date for historical reasons.
        endDate          - Now.

    Returns:
        The dirty dozen for the requested category, name, and date range.
    """
    location_category = request.args.get('locationCategory',
                                         default='site',
                                         type=str)
    location_category = 'site_name' if location_category == 'site' else location_category

    location_name = request.args.get('locationName',
                                     default='Union Beach',
                                     type=str)
    start_date = request.args.get('startDate',
                                  default='2016-1-1',
                                  type=str)
    end_date = request.args.get('endDate',
                                default=datetime.now().strftime('%Y-%m-%d'),
                                type=str)

    return jsonify(dirtydozen=coa_logic.dirty_dozen(location_category,
                                                    location_name,
                                                    start_date,
                                                    end_date))


@APP.route('/breakdown')
def breakdown() -> JSON:
    """
    The breakdown route is designed to give the UI the data
    for a breakdown.

    The app route itself contains:
        locationCategory - Default of site.
        locationName     - Default of the common location.
        startDate        - The old start date for historical reasons.
        endDate          - Now.

    Returns:
        The breakdown for the requested category, name, and date range.
    """
    location_category = request.args.get('locationCategory',
                                         default='site',
                                         type=str)
    location_category = 'site_name' if location_category == 'site' else location_category

    location_name = request.args.get('locationName',
                                     default='Union Beach',
                                     type=str)
    start_date = request.args.get('startDate',
                                  default='2016-1-1',
                                  type=str)
    end_date = request.args.get('endDate',
                                default=datetime.now().strftime('%Y-%m-%d'),
                                type=str)

    return jsonify(data=coa_logic.breakdown(location_category,
                                            location_name,
                                            start_date,
                                            end_date))


@APP.route('/validdaterange')
def valid_date_range() -> JSON:
    """
    The valid date range route is designed to give the UI a valid date
    range.

    The app route itself contains:
        locationCategory - Default of site.
        locationName     - Default of the common location.

    Returns:
        The valid date range for the requested category and name.
    """
    location_category = request.args.get('locationCategory',
                                         default='site',
                                         type=str)
    location_category = 'site_name' if location_category == 'site' else location_category

    location_name = request.args.get('locationName',
                                     default='Union Beach',
                                     type=str)

    return jsonify(validDateRange=coa_logic.valid_date_range(location_category,
                                                             location_name))

@APP.route('/locationsHierarchy')
def locations_hierarchy() -> JSON:
    """
    The locations hierarchy route returns the all the locations in a hierarchy.

    Returns:
        A json list of the locations hierarchy.
    """
    return jsonify(locationsHierarchy=coa_logic.locations_hierarchy())

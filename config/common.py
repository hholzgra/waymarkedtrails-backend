# SPDX-License-Identifier: GPL-3.0-only
#
# This file is part of the Waymarked Trails Map Project
# Copyright (C) 2015-2020 Sarah Hoffmann

#############################################################################
#
# Database settings

import os.path as op

DB_NAME = 'planet'
DB_USER = None
DB_PASSWORD = None
DB_RO_USER = 'www-data'
DB_NODESTORE = None

REPLICATION_URL='https://planet.openstreetmap.org/replication/minute/'
REPLICATION_SIZE=50


#############################################################################
#
# Common options for map styles

MEDIA_DIR = 'data'

DB_SCHEMA = None
DB_SRID = 3857

GUIDEPOSTS = None
NETWORKNODES = None

#############################################################################
#
# Configuration classes to be used in derived config

class RouteDBTables(object):
    country = 'country_osm_grid'
    change = 'changed_objects'
    route_filter = "filtered_relations"
    way_relation = "way_relations"
    segment = 'segments'
    hierarchy = 'hierarchy'

class SlopeDBTables(RouteDBTables):
    joinedway = 'joined_slopeways'
    way_table = 'slopeways'

class GuidePostConfig:
    table_name = 'guideposts'
    node_subset = 'tags @> \'{ "tourism" : "information", "information": "guidepost"}\'::jsonb'
    subtype = None
    require_subtype = False

class NetworkNodeConfig:
    table_name = 'networknodes'
    node_tag = 'ref'

class RouteTableConfig(object):
    table_name = 'routes'

    network_map = {}
    tag_filter = None
    symbols = None

class PisteTableConfig(object):
    table_name = 'routes'
    symbols = None

    difficulty_map = {'novice'       : 1,
                      'easy'         : 2,
                      'intermediate' : 3,
                      'advanced'     : 4,
                      'expert'       : 5,
                      'extreme'      : 6,
                      'freeride'     : 10,
                      # unknown value: 0
                     }

    piste_type = {'downhill'      : 1,
                  'nordic'        : 2,
                  'skitour'       : 3,
                  'sled'          : 4,
                  'hike'          : 5,
                  'sleigh'        : 6,
                  # unknown value : 0
                 }


#############################################################################
#
# Local settings

try:
    from config.local import *
except ImportError:
    pass # no local settings provided


#############################################################################
#
# Basic render settings

if globals().get('TILE_CACHE') is None:
    TILE_CACHE = {
        'type' : "PostgresCache",
        'empty_tile' : { 'png' : op.join(MEDIA_DIR, 'symbols/misc/empty.png') },
        'dba' : 'dbname=tiles',
        'max_zoom' : 15
    }

if globals().get('RENDERER') is None:
    RENDERER = {
        'source_type' : 'xml',
        'tile_size' : (256, 256),
        'max_zoom' : 18
    }



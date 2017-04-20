#!/usr/bin/env python

import apache_beam
import configobj
import json

from options import SetPipelineOptions

class ReadStreams:
    streams_path = configobj.ConfigObj("sfm.conf").get('standard').get('streams')    

    def read_streams(self, pipeline):
        return (pipeline 
             | 'read streams' >> apache_beam.io.ReadFromText(self.streams_path)
        ) 

    def map_streams(self, pipeline):
        return (pipeline
             | 'map streams' >> apache_beam.Map(lambda user_id: (json.loads(user_id).get('user_id'), json.loads(user_id)))
        )

class GroupStreams:
    def group_streams_with_tracks(self, streams, tracks):
        # s = (({'streams':s, 'tracks':t}) | 'co group by key tracks' >> ab.CoGroupByKey(pipeline=p))
        return None

    def group_streams_with_users(self, streams, users):
        return (({'streams': streams, 'users': users})
            | 'co group by key user_id' >> apache_beam.CoGroupByKey()
        ) # (({'streams':s,'users':u}) | 'co group by key users' >> ab.CoGroupByKey())

    def remap_streams(self, streams):
        return (streams
            | 'remap streams' >> apache_beam.Map(lambda streams: (json.loads(streams).get('track_id'), json.loads(streams)))
        )

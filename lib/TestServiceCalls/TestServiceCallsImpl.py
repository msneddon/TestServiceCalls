# -*- coding: utf-8 -*-
#BEGIN_HEADER
import os
from biokbase.workspace.client import Workspace
#END_HEADER


class TestServiceCalls:
    '''
    Module Name:
    TestServiceCalls

    Module Description:
    A KBase module: TestServiceCalls
    '''

    ######## WARNING FOR GEVENT USERS #######
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    #########################################
    VERSION = "0.0.1"
    GIT_URL = ""
    GIT_COMMIT_HASH = ""
    
    #BEGIN_CLASS_HEADER

    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.workspaceURL = config['workspace-url']
        self.shockURL = config['shock-url']
        self.handleURL = config['handle-service-url']
        self.sharedFolder = config['scratch']
        #END_CONSTRUCTOR
        pass
    

    def get_feature_ids(self, ctx, p):
        """
        :param p: instance of type "Params" (Insert your typespec information
           here.) -> structure: parameter "ref" of String
        :returns: instance of type "Output" -> structure:
        """
        # ctx is the context object
        # return variables are: o
        #BEGIN get_feature_ids
        ws = Workspace(self.workspaceURL)

        featureContainers = ws.get_object_subset([{
                                     'included':['feature_container_references'], 
                                     'ref':p['ref']}])[0]['data']['feature_container_references']

        all_features = {}
        for fc in featureContainers:
            fc_ws_id = featureContainers[fc]
            features = ws.get_object_subset([{
                                     'included':['/features/*/feature_id'], 
                                     'ref':fc_ws_id}])[0]['data']['features']
            all_features[fc] = features.keys()
            #feature_list = []
            #for f in features:
            #    feature_list.append(features[f]['feature_id'])
            #all_features[fc] = feature_list

        o = all_features
        #END get_feature_ids

        # At some point might do deeper type checking...
        if not isinstance(o, dict):
            raise ValueError('Method get_feature_ids return value ' +
                             'o is not type dict as required.')
        # return the results
        return [o]

    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK", 'message': "", 'version': self.VERSION, 
                     'git_url': self.GIT_URL, 'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]

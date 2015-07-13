#!/usr/bin/env python
from SceneGraph import options
from SceneGraph.core.nodes import DagNode


SCENEGRAPH_NODE_TYPE = 'default'


class Default(DagNode):

    default_name  = 'default'
    default_color = [172, 172, 172, 255] 

    def __init__(self, *args, **kwargs):
        kwargs.update(node_type=SCENEGRAPH_NODE_TYPE)        
        DagNode.__init__(self, *args, **kwargs)


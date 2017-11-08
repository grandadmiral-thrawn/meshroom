import sys
from meshroom.core import desc


class PrepareDenseScene(desc.CommandLineNode):
    internalFolder = '{cache}/{nodeType}/{uid0}/'
    commandLine = 'aliceVision_prepareDenseScene {allParams}'

    inputs = [
        desc.File(
            name='input',
            label='Input',
            description='''SfMData file.''',
            value='',
            uid=[0],
        ),
        desc.ChoiceParam(
            name='scale',
            label='Scale',
            description='''Image downscale factor.''',
            value=2,
            values=[1, 2, 4, 8, 16],
            exclusive=True,
            uid=[0],
        ),
        desc.ChoiceParam(
            name='verboseLevel',
            label='Verbose Level',
            description='''verbosity level (fatal, error, warning, info, debug, trace).''',
            value='info',
            values=['fatal', 'error', 'warning', 'info', 'debug', 'trace'],
            exclusive=True,
            uid=[0],
        ),
    ]

    outputs = [
        desc.File(
            name='ini',
            label='MVS Configuration file',
            description='',
            value='{cache}/{nodeType}/{uid0}/_tmp_scale{scaleValue}/mvs.ini',
            uid=[],
            group='',  # not a command line arg
        ),

        desc.File(
            name='output',
            label='Output',
            description='''Output directory.''',
            value='{cache}/{nodeType}/{uid0}/',
            uid=[],
        )
    ]

from meshroom.core import desc

class Texturing(desc.CommandLineNode):
    internalFolder = '{cache}/{nodeType}/{uid0}/'
    commandLine = 'CMPMVS {mvsConfigValue} --texturing'
    cpu = desc.Level.INTENSIVE
    ram = desc.Level.INTENSIVE

    mvsConfig = desc.File(
            label='MVS Configuration file',
            description='',
            value='',
            uid=[0],
            isOutput=False,
            )
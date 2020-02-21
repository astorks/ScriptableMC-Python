class PythonPlugin:
    pluginName = "PythonPlugin"

    def getServer(self):
        return self.context.getServer()

    def registerEvent(self, type, callback):
        return self.context.registerEvent(type, callback)

    def newCommand(self, name):
        return self.context.newCommand(name);
    
    def unregisterCommand(self, command):
        return self.context.unregisterCommand(command);
    
    def registerCommand(self, command):
        return self.context.registerCommand(command);


class TestPythonPlugin(PythonPlugin):
    def __init__(self):
        self.pluginName = "TestPythonPlugin"

    def onLoad(self):
        print("TestPythonPlugin.onLoad()")

    def onEnable(self):
        print("TestPythonPlugin.onEnable()")
        self.cmd = self.newCommand("hellopy");
        self.cmd.setExecutor(self.onHelloWorldCmdExecute);
        self.registerCommand(self.cmd);

    def onDisable(self):
        print("TestPythonPlugin.onDisable()")

    def onHelloWorldCmdExecute(self, sender, command, label, args):
        sender.sendMessage("Hello World from Python!")
        print("TestPythonPlugin.onHelloWorldCmdExecute()")
        return False

[
    TestPythonPlugin
]
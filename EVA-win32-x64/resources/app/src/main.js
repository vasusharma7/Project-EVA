const electron = require("electron");
const { Menu, app, Tray, BrowserWindow, ipcMain: ipc } = electron; //Inter Process Communication
const exec = require("child_process").exec;
const child_process = require("child_process");
var { PythonShell } = require("python-shell");
const path = require("path");
var options = {};
function execute(command, callback) {
  exec(command, (error, stdout, stderr) => {
    callback(stdout);
  });
}
let tray = null;

// exec("ls -la", (error, stdout, stderr) => {
//     if (error) {
//         console.log(`error: ${error.message}`);
//         return;
//     }
//     if (stderr) {
//         console.log(`stderr: ${stderr}`);
//         return;
//     }
//     console.log(`stdout: ${stdout}`);
// });

// execute('python -c "import sys; print(sys.executable)"', (output) => {
// pythonHome = String(output).replace("\\", "/");
// console.log(pythonHome.replace("\\", "/"));
// options = {
//   // mode: "text",
//   pythonPath:
//     "C:/Users/Vasu/AppData/Local/Programs/Python/Python37/python.exe",
//   // pythonPath:'/usr/bin/python3'
//   // pythonOptions: ["-u"],
//   // args: ['value1', 'value2', 'value3']
// };
// });
options = {
  // mode: "text",
  //pythonPath:"mypython/Scripts/python.exe",
//  pythonPath:"C:/Users/soham/Desktop/PPL_Project_2020-parekh0711-patch-1/bot/bot/EVA-win32-x64/resources/app/src/mypython/Scripts/python.exe",
//  scriptPath:"python/myenv/Scripts",
 pythonPath: "C:/Users/soham/AppData/Local/Programs/Python/Python38/python.exe",
  //pythonPath:'/usr/bin/python3'
  // pythonOptions: ["-u"],
  // args: ['value1', 'value2', 'value3']
};
var mode = "asst";
var manage = {
  state: -1,
  stateListener: function (val) {},
  set trigger(val) {
    this.state = val;
    this.stateListener(val);
  },
  get trigger() {
    return this.state;
  },
  registerListener: function (listener) {
    this.stateListener = listener;
  },
};

require("electron-reload")(__dirname, {
  electron: require(`${__dirname}/../node_modules/electron`),
});

var mainWindow = null;
app.on("ready", async (_) => {
  mainWindow = new BrowserWindow({
    width: 550,
    height: 300,
    resizeable: false,
    transparent: true,
    frame: false,
    webPreferences: {
      nodeIntegration: true,
    },
  });
  mainWindow.setResizable(false);
  mainWindow.setMenuBarVisibility(false);
  // mainWindow.setAlwaysOnTop(true);
  mainWindow.loadURL(`file://${__dirname}/index.html`);

  tray = new Tray(path.join(__dirname, "assets/eva.png"));
  const contextMenu = Menu.buildFromTemplate([
    {
      label: "EVA",
      click: function () {
        mainWindow.show();
      },
    },
    {
      label: "Quit",
      click: function () {
        mainWindow.quit();
        app.quit();
      },
    },
  ]);
  tray.on("click", () => {
    mode="asst"
    manage.trigger+=1
    mainWindow.show();
  });
  // tray.on("click", () => {
  //   mode="asst"
  //   manage.trigger+=1
  //   mainWindow.show();
  // });
  tray.setToolTip("EVA - Your Personal Buddy");
  tray.setContextMenu(contextMenu);
  // mainWindow.webContents.openDevTools();

  // manage.registerListener(() => {
  //   console.log("CALLING SCRIPT");
  //   var python = child_process.spawn("python", ["./ppl/chat.py"]);
  //   python.stdout.on("data", function (data) {
  //     console.log("PYTHON");
  //     console.log(data.toString("utf8"));
  //     python.kill();
  //     manage.trigger += 1;
  //   });
  // });
  // manage.trigger += 1;

  manage.registerListener(() => {
    console.log("CALLING SCRIPT");
    if (mode == "asst") {
      PythonShell.run(path.join(__dirname, "../ppl/bot.py"), options, function ( //bot.py
        err,
        results
      ) {
        if (err) {
          throw err;
          return;
        }
        if (results.length > 3) {
          mainWindow.webContents.send("displayResponse", results); //event mirror isntance
        }
        console.log("results: ", results);
        manage.trigger += 1;
      });
    }
    if (mode == "chat") {
      PythonShell.run(
        path.join(__dirname, "../ppl/chat.py"),
        options,
        function (err, results) {
          if (err) throw err;
          if (results.length > 3) {
            mainWindow.webContents.send("displayResponse", results); //event mirror isntance
          }
          console.log("results: ", results);
          manage.trigger += 1;
        }
      );
    }
    // if (mode == "sleep") {
    //   PythonShell.run(
    //     path.join(__dirname, "../ppl/sleep.py"),
    //     options,
    //     function (err, results) {
    //       if (err) throw err;
    //       if (results[0] == "Activate") {
    //         mainWindow.show()
    //         mode="asst"
    //       }
    //       console.log("results: ", results);
    //       manage.trigger += 1;
    //     }
    //   );
    // }
  });
  manage.trigger += 1;

  // pyshell.on("message", function (message) {
  //   // received a message sent from the Python script (a simple "print" statement)
  //   console.log(message);
  // });

  mainWindow.on("closed", (_) => {
    mainWindow = null;
  });
});

app.on("window-all-closed", () => {
  if (process.platform !== "darwin") {
    app.quit();
  }
});

ipc.on("startAsst", (evt) => {
  mode = "asst";
});
ipc.on("startChat", (evt) => {
  mode = "chat";
});

ipc.on("close", (evt) => {
  app.quit();
});

ipc.on("min", (evt) => {
   mode="sleep"
  mainWindow.hide();
});

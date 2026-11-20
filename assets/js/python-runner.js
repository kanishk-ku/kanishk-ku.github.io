
let pyodideInstance = null;

async function initializePython() {
  if (pyodideInstance) return pyodideInstance;

  const output = document.getElementById("python-output");
  output.textContent = "Loading Python environment...";

  try {
    pyodideInstance = await loadPyodide({
      indexURL: "https://cdn.jsdelivr.net/pyodide/v314.0.8/full/"
    });

    pyodideInstance.setStdout({
      batched: (message) => {
        output.textContent += message + "\n";
      }
    });

    pyodideInstance.setStderr({
      batched: (message) => {
        output.textContent += message + "\n";
      }
    });

    output.textContent = "Python is ready!";
    return pyodideInstance;
  } catch (error) {
    output.textContent = "Initialization error: " + error;
    throw error;
  }
}

async function runPython() {
  const editor = document.getElementById("python-code");
  const output = document.getElementById("python-output");

  try {
    const pyodide = await initializePython();
    output.textContent = "";

    await pyodide.runPythonAsync(editor.value);

  } catch (error) {
    output.textContent += "\nError: " + error;
  }
}

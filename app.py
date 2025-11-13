from flask import Flask
import subprocess

app = Flask(__name__)

# 1) Option A: put your script logic directly here
def run_my_script():
    # TODO: replace this with your real code
   subprocess.run(["python", "simple.py"], check=True)
    # example:
    # import my_script
    # my_script.main()

# 2) Option B: call an external script file like my_script.py
# def run_my_script():
#     subprocess.run(["python", "my_script.py"], check=True)

@app.route("/run")
def run():
    try:
        run_my_script()
        return "OK", 200
    except Exception as e:
        # basic error logging
        print("Error:", e)
        return "ERROR", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

from flask import Flask, render_template, request
import model

app = Flask(__name__)

@app.route('/hello', methods=['GET', 'POST'])
def hello():
    tmpStr = "hello world"
    tmpList = [1, 2, 3, 4, 5]
    return render_template('tmpStr.html', tmpStr=tmpStr
                                        , request_method=request.method
                                        , tmpList=tmpList)

@app.route('/show_staff')
def show_staff():
    staff_data = model.getStaff()
    column = ['ID', 'Name', 'DeptId', 'Age', 'Gender', 'Salary']
    return render_template('show_staff.html', column=column
                                            , staff_data=staff_data)

if __name__ == '__main__':
    app.run()
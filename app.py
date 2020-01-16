from flask import Flask,make_response,render_template
import pdfkit
from pyvirtualdisplay import Display


app =   Flask(__name__)


@app.route("/<string:name>/<string:location>")
def index(name,location):
    try:
        Display().start()
        rendered    =   render_template("templates_pdf.html",name=name,location=location)
        pdf         =   pdfkit.from_string(rendered,False)
        

        response    =   make_response(pdf)
        response.headers['Content-Type']    =   'application/pdf'
        response.headers['Content-Disposition']    =   'attachment; filename=output.pdf'
    finally:
        Display().stop()
    return response 


if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template,request
import logging
import os
app = Flask(__name__)
logging.basicConfig(level=logging.INFO)


@app.route('/', methods=['GET'])
def home_page():
    logging.info(100*'*')
    logging.info("Method : home_page")
    try:
        return render_template('index.html')
        logging.info("Home page displayed Successfully")
    except Exception as e:
        logging.critical(e, exc_info=True)
        logging.error("Failed to display Homepage")
    logging.info("Exiting Method : home_page")
    logging.info(100*'*')


@app.route('/math', methods=['POST'])  # This will be called from UI
def base_aggregator():
    logging.info(100*'*')
    logging.info('method : base_aggregator')
    if (request.method=='POST'):

        # show_road, check_box variable if set to 1,
        # displays road
        show_road = request.form.get('building')
        if show_road is not None:
            show_road = int(show_road)
        else:
            show_road = 0

        '''
        plot variable if checked shows only plot 
        '''
        plot = request.form.get("plot")
        if plot is not None:
            plot = int(plot)
        else:
            plot = 0

        area = int(request.form['area'])
        breadth = int(request.form['breadth'])
        length = int(area/breadth)
        road = int(request.form['Road'])
        '''
        The variables have been renamed for 
        clearer understandability
        '''
        front = length
        side = breadth
        if plot == 1:
            os.system('python only_plot.py {} {}'.format(front, side))
            return render_template('index.html')


    logging.info('Exiting method : base_aggregator')
    logging.info(100*'*')
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)



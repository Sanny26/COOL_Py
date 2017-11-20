# COOL2Py
It builds a  translator that converts COOL language to python.
_______________________________________________________________________
**Instructions to setup the translator**

* Download the source code for the translator.
* Install ply python package.

    ```pip3 install ply```

* Example cool files are available in `examples/` folder  

___________________________________________________________________________

**Instructions to run the translator:**

* Run the translator as

     `./translator.py <filename.cl> > <outputfile.py>`
* Output will be generated in the `outputfile.py` file.
* Please make sure to include the `base.py` file that contains basic COOL libraries converted to python, before running the Output.
* Run the converted file as `python3 outputfile.py`

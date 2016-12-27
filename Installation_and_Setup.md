This will be an interactive workshop so be sure to come with a laptop prepared to try out some of the tools that will be discussed and demoed.

First, download this repository by either doing:

    git clone http://github.com/spacetelescope/aas229_workshop.git

or by downloading and then expanding the repository file.

Then, cd into the aas229_workshop directory.

If you don't already have Anaconda installed, install the the Anaconda distribution for Python 3.5, which we have packaged along with some additional software. Downloads for Mac and Linux can be found at:

    http://ssb.stsci.edu/conda/installers/AstroConda-1.0.2-Linux-x86_64.sh
    http://ssb.stsci.edu/conda/installers/AstroConda-1.0.2-MacOSX-x86_64.sh

Note: please do this ahead of the workshop if possible.

These include both Anaconda and the AstroConda software repository, which contains additional tools that will be shown at the workshop. If you have trouble installing using the above files (or are using Windows), you will need to download anaconda separately (https://www.continuum.io/downloads), and then install Astroconda on top following the instructions here: http://astroconda.readthedocs.io/en/latest/.

If you have Anaconda already installed, and have not used the shell installer above, you can create a special environment for this workshop which contains all the software you will need using the environment file below. If you've already used the installer above you should already have all the software you need on your machine:

    % conda env create -n aas229-workshop --file environment.yml
    % source activate aas229-workshop

Note: you need to be inside the aas229_workshop directory for this to work.

The command above will create an environment called "aas229-workshop", but you can change that to any other desirable name.

Note for windows users: you can use the environment_win.yml file instead, this will not include the ginga or imexam packages:

    % conda env create -n aas229-workshop --file environment_win.yml
    % source activate aas229-workshop


You can run the check_env.py script to perform a basic check of your Python environment and some of the required dependencies:

    % python check_env.py
If you have issues getting set up, you can also run the notebooks on mybinder.org:

[![Binder](http://mybinder.org/badge.svg)](http://mybinder.org:/repo/spacetelescope/aas229_workshop)

This will be an interactive workshop so be sure to come with a laptop prepared to try out some of the tools that will be discussed and demonstrated.

If you have any problem with the instructions here, please open an issue at https://github.com/spacetelescope/aas229_workshop/issues/

# 1. Clone This Repository

First, download this repository by either doing:

    % git clone http://github.com/spacetelescope/aas229_workshop.git

or by downloading and then expanding the repository file.

Then, cd into the aas229_workshop directory.

# 2. Install Anaconda, AstroConda

Note: please do this ahead of the workshop if possible.

## 2a. No Anaconda

### Mac, Linux

If you don't already have Anaconda installed, install the the Anaconda distribution for Python 3.5, which we have packaged along with some additional software. Downloads for Mac and Linux can be found at:

    http://ssb.stsci.edu/conda/installers/AstroConda-1.0.2-Linux-x86_64.sh
    http://ssb.stsci.edu/conda/installers/AstroConda-1.0.2-MacOSX-x86_64.sh

These shell installers include both Anaconda and the AstroConda software repository, which contains additional tools that will be shown at the workshop.

If you have trouble installing using the above files, you will need to download Anaconda separately (https://www.continuum.io/downloads). Then, proceed to Step 2b.

More information about AstroConda can be found at http://astroconda.readthedocs.io/en/latest/ (currently does not support Windows build).

### Windows

You will need to download Anaconda separately (https://www.continuum.io/downloads). Then, proceed to Step 2b.

## 2b. Already Has Anaconda (or Step 2a Failed)

If you have Anaconda already installed, have not used the shell installer in Step 2a (or it failed), and have not already installed the Astroconda software package, then follow this step. If you've already used the installer in Step 2a, you should already have all the software you need on your machine and you can skip this step.

Note: You need to be inside the aas229_workshop directory for this to work.

The command below will create an environment called "aas229-workshop", but you can change that to any other desirable name by replacing the quoted name.

### Mac, Linux

You can create a special environment for this workshop which contains all the software you will need using the environment file below:

    % conda env create -n aas229-workshop --file environment.yml
    % source activate aas229-workshop

### Windows

You can create a special environment for this workshop which contains most of the software you will need using the environment file below:

    % conda env create -n aas229-workshop --file environment_win.yml
    % activate aas229-workshop

Then, you can install the rest of the packages using:

    % pip install -r pip_requirements_win.txt

Note: Windows distribution currently does not yet support imexam.

# 3. Check Installation

Note: You need to be inside the aas229_workshop directory for this to work.

You can run the check_env.py script to perform a basic check of your Python environment and some of the required dependencies:

    % python check_env.py

# 4. Pick Up Changes

To pick up any updates for workshop materials, make sure you are in the aas229_workshop directory and then use the following commands:

    % git fetch origin master
    % git rebase origin/master
    
The commands above only work if you used git in Step 1. The rebase command will not work properly if you have modified the materials (e.g., running the notebooks). In that case or if you downloaded the materials manually, you will have to update the changed files manually as well; e.g., by downloading the updated file (the RAW format) via GitHub web interface.

Software covered in this workshop should not need any more updates after Steps 2 and 3. However, in the event of any necessary quick fix, instructions will be given out during the workshop (e.g., using conda or pip commands).

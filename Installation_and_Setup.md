This is an interactive workshop so be sure to come with a laptop prepared to try out some of the tools that will be discussed and demonstrated.

### If you already have many of these packages installed,  check to see if there have been any new version releases::

You can update all the software in your environment using:

    % conda update --yes --all

You can also update individual packages with conda update, these are the two packages with recent releases:

    % conda update -c http://ssb.stsci.edu/astroconda stginga
    % conda update -c http://ssb.stsci.edu/astroconda imexam

If you have any problem with the instructions here, please open an issue at https://github.com/spacetelescope/aas229_workshop/issues/

# 1. Clone This Repository

First, download this repository by either doing:

    % git clone http://github.com/spacetelescope/aas229_workshop.git

or by downloading and then expanding the repository file. Github allows for downloading a ZIP file, click on the green "Clone or Download" button on the front page and select zip file. Save the zip file to a reasonable directory and unpack it. 


# 2. Install Anaconda for your operating system here:

https://www.continuum.io/downloads

    Note: Please do this ahead of the workshop if possible.

Proceed to Step 3 after you have installed Anaconda. Make sure that from here out you are using a bash shell, the activate command which manages the environments only supports posix-compliant shells like bash and zsh. It's still possible to use csh, however you will need to ammend your path by hand.

You may also choose to install Miniconda, which is the same as Anaconda,  but it comes with fewer default packages so it's faster to download and takes up less space. More information can be found here:

http://conda.pydata.org/docs/install/quick.html

## 2a. Optionally install Astroconda

Astroconda contains all the software packages delivered by Space Telescope.  More information about AstroConda can be found at http://astroconda.readthedocs.io/en/latest/ (currently does not support Windows build).

If you only want to install the smaller subset of packages used in this workshop you can proceed to step 3.

When you install AstroConda, it is a good idea to make a separate envrionment whch will contain all the software. The installation instructions for Astroconda will be
similar to step 3 below. If you want to create another special environment just for the workshop, after you install astroconda, close the environment you are in by issuing the  "source deactivate" command, then follow the instructions for step 3.

You should not have to do the step of adding the astroconda channel information since it will have alraedy been done.


# 3. Create an  Anaconda environment for the workshop

If you have Anaconda already installed you can skip Step 2. and go straight on to this step.

Note: First make sure you are working in a bash shell (not tcsh or csh) and change into the aas229_workshop directory.

The command below will create an environment called "aas229-workshop", but you can change that to any other desirable name by replacing the quoted name and editing the name in the environment file.

### Mac, Linux

You can create a special environment for this workshop which contains all the software you will need using the environment file below:

    % conda config --add channels http://ssb.stsci.edu/astroconda
    % conda env create -n aas229-workshop --file environment.yml
    % source activate aas229-workshop

### Windows

You can create a special environment for this workshop which contains most of the software you will need using the environment file below:

    % conda config --add channels http://ssb.stsci.edu/astroconda
    % conda env create -n aas229-workshop --file environment_win.yml
    % activate aas229-workshop

Then, you can install the rest of the packages using:

    % pip install -r pip_requirements_win.txt

Note: Windows distribution currently does not yet support imexam with DS9. However, all the imexam functionality including image viewing can be used with Ginga as the viewer. 

# 4. Check Installation

Note: You need to be inside the aas229_workshop directory for this to work.

You can run the check_env.py script to perform a basic check of your Python environment and some of the required dependencies:

    % python check_env.py

If the script reports that some of the versions don't match, you can update the reported packages using the ``conda update`` method described up top, namely:


    % conda update <packagename>

    or

    % conda update packagename=version


# 5. Pick Up Changes to the workshop repository:

## 5a. Using git

To pick up any updates for workshop materials, make sure you are in the aas229_workshop directory and then use the following command:

    % git pull

This *may* result in an error, if you've modified any of the files that have changed since you last pulled from git.  In that case, you'll need to do:

    % git fetch origin master
    % git reset --hard origin/master

NOTE: This will overwrite any notebooks you've modified.  Be sure to back up any changes you care about.  Or if you really want to keep something, you can ask one of the instructors to show you how to do a more fine-grained update using advanced git commands.

## 5b. Manual Download 

The commands above only work if you used git in Step 1.  If you downloaded the materials manually, you will have to update the changed files manually; e.g., by downloading the updated file (the RAW format) via GitHub web interface, or by downloading and unpacking a new zip file.

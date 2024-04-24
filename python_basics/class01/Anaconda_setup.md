# Anaconda and Conda environment set up
## Install anaconda
**Anaconda** is a distribution of packages built for data science. It comes with conda, a package and environment manager. We can use conda to create environments for isolating your projects which use different versions of packages such as python. We can also use it to install, uninstall, manage, and update packages in our environments. 

Anaconda is available for Windows, Mac OS X, and Linux. You can **download the installers and installation instructions at [here](https://www.anaconda.com/products/distribution)**. Choose the installation based on your operating system.

Choose the Python 3 version. Also, choose the 64-bit installer if you have a 64-bit operating system, otherwise go with the 32-bit installer. 

After installation, you’re automatically in the default conda environment with all packages installed. You can check out your own install by entering `conda list` into your terminal.

For Windows user, open the Anaconda Prompt application. For Mac user, use your terminal on Mac. In the prompt, run the following commands:

```
conda upgrade --all
# this step takes forever, so if in hurry, do it later.
```

Answer `yes` when asked if you want to install the packages. The packages that come with the initial install tend to be out of date, so updating them now will prevent future errors from out of date software.

#####Troubleshooting#####

If you are using ZShell and seeing the following error message:

```
conda command not found
```

you'll need to do the following (replacing `[your_username]` with your username on your computer):

Add ```export PATH="/Users/[your_username]/anaconda/bin:$PATH"``` to your .zsh_config file.

## Manage environment and packages
### Create an environment
To create an environment, use `conda create -n env_name [list of packages]` in your terminal. 

i.e.:

```
conda create -n intro python=3
# (intro is a name I give for ou class. Feel free to choose another name.)
```

When prompted `The following NEW packages will be INSTALLED`, enter `y` to proceed.

When creating an environment, you can specify which version of Python to install in the environment. This command installs the most recent version of Python 3. To install a specific version, for example you can use `conda create -n itds python=3.9` for Python 3.9.

### Enter and leave the environment
Use `conda activate intro` or `source activate intro` to enter the environment you just created on Mac OSX/Linux. 
On Windows, use `activate intro`.

To leave the environment, use `conda deactivate` or `source deactivate` (the latter command may give you error message sometimes depending on your setting) on OSX/Linux. 
On Windows, use `deactivate`.

For the next steps, let's activate and stay in the `intro` environment.

### Install packages
When you are in the environment, you'll see the environment name in the terminal prompt like below. 

```
(intro) Macbook:ds-intro-class user$ 
```

The environment has only a few packages installed by default, plus the ones you installed when creating it. You can check this out with `conda list`. Installing packages in the environment is: `conda install [package_name]`. The specific packages you install will only be available when you're in the environment. 

### Saving and loading environments
A really useful feature is sharing environments so others can install all the packages used in your code, with the correct versions. You can save the packages info to a YAML file with `conda env export > environment.yml` command in your terminal. The first part `conda env export` writes out all the packages in the current environment, including the Python version to the YAML file named `environment.yml`.

To create an environment from an environment YAML file simply use `conda env create -f environment.yml`. This will create a new environment with the same name listed in the `environment.yml` file.

You can also create a `pip` file (usually named `requirements.txt` using `pip freeze` for people not using `conda`.

### Listing environments
If you forget what your environments are named , use `conda env list` to list out all the environments you've created. You should see a list of environments, there will be an asterisk(*) next to the environment you're currently in.

### Removing environments
If there are environments you don't use anymore, `conda env remove -n env_name` will remove the specified environment.

### Summary
So here are the commands we want to run to create the environment we need for this class (and a few command to play around to check things are happening as expected along the way):

```
# (using MAC)
conda create -n intro python=3
conda env list
conda activate intro
conda list
conda install numpy pandas jupyter notebook git matplotlib seaborn pandas-profiling scipy
conda list
conda env export > environment.yml
cat environment.yml
conda deactivate
conda env list

# windows should be similar with some modification
```

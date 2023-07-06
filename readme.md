# Realty With Ease

Realty with Ease is a fully featured web application that aims to automated solutions to Real Estate problems in the Nigerian Space
<br>

# Project Pre-requisites

- [Django v4.2.2](https://www.djangoproject.com/)
- [Python v 3.11.4](https://www.python.org/)
- [PostgresQL 15](https://www.postgresql.org/)
- [Pipenv](https://pypi.org/project/pipenv/)

<br>

# Project Setup

- Clone to the repository to your local machine
- Run the command, `pipenv install` to install all dependencies
- Create a project environment variables file, `.env`, copy the contents of `.env.example` into it
- Create test environment variables file, `.env.test`, copy the contents of `.env.test.example` into it
- Input the missing environment variables
- Enter a new pipenv environment shell with `pipenv shell`
- Set up the database by running migrations using the command, `python manage.py migrate`
- Start up the project using the command, `python manage.py runserver`
- You should now be able to access the server via the endpoint URL - **[http://localhost:8000](http://localhost:800)**

<br>

# Version Control Management

The codebase is managed using GIT, and the branch management philosophy is a hybrid of Gitflow called HubFlow. HubFlow
seeks to integrate a seamless workflow where teams can utilize GitFlow against the GitHub Online Infrastructure.

## HubFlow Installation

### Windows

To install Hubflow on your local machine, run the following commands in a terminal with administrator privileges.

Default git install directory is: `C:\Program Files\Git`

1. Clone hubflow into a convenient location

   `git clone https://github.com/datasift/gitflow hubflow`

2. run the following commands

```
cd hubflow

cp git-hf* "C:\Program Files\Git\cmd\"
cp hubflow-common "C:\Program Files\Git\cmd\"

git submodule update --remote --init --checkout
cp shFlags/src/shflags "C:\Program Files\Git\cmd\hubflow-shFlags"
```

### Mac or Linux Based

To install HubFlow on your local machine, you can run the following commands anywhere on your machine outside the
project folder

```
git clone https://github.com/datasift/gitflow
cd gitflow
sudo ./install.sh
sudo git hf upgrade
```

To test the installation and list the available commands, run the following:

```
git hf help
```

## HubFlow Commands

### 1. Initialize HubFlow Tools (Run within the project folder)

```
git hf init -af
```

Populate the necessary values i.e.

- `main` branch for the most stable version of the project that can be deployed to production.
- `develop` branch for development which acts as the base branch for all feature development.
- `feature` branch for implementing new features and serves to isolate development without disrupting the stability of
  the codebase
- `release` branch for features that are ready to be deployed. Only bug fixes and docs should be added to this branch
- `hotfix` branch for quickly fixing critical issues/bugs in the main branch that require an immediate patch.
- `support`branch for long-lived branches that are aimed at maintaining older versions of the codebase no longer
  actively being developed
- `version` prefix tag is used to uniquely identify releases, this should be left **BLANK** with no values in it.\

### 2. Create a feature branch

```
git hf feature start <FEATURE_BRANCH_NAME>
```

If you are starting to work on an existing feature branch, do this:

```
git hf feature checkout <FEATURE_BRANCH_NAME>
```

### 3. Publish the feature branch

```
git hf push
```

Once you have completed your feature implementation, initiate a pull request on the GitHub Repository from
your `feature` branch into the `dev` branch, only after your PR has been merged into `dev` can you close out the feature
branch locally on your machine. This is called a **FEATURE FINISH**

### 4. Finish the feature branch

```
git hf feature finish <FEATURE_BRANCH_NAME>
```

<br>

For more details about the other commands, visit - https://datasift.github.io/gitflow/GitFlowForGitHub.html

<br>

# Release Strategy

After successfully merging a feature, initiating a release is necessary. The release strategy must align with the
various contexts existing within the codebase, such as the Client, Admin, and Public API. If the feature belongs to a
sprint, the semantic versioning patch point should be incremented. If the sprint is completed, the semantic versioning
minor point must be updated. For example:

- Client - `client@v1.0.0`
- Admin - `admin@v1.0.1`

For each release, the environment variable called `CURRENT_PROJECT_RELEASE` in the `.env` and `.env.example` files as
well as the version number in the `package.json` file should be updated. The value should align with the release based
on the context, for example:

`CURRENT_PROJECT_RELEASE = 'client@v1.0.2'`

`"version": "1.0.2"`

This provides better visibility into regression testing for our releases and enables us to track any issues with a
specific release via Sentry.

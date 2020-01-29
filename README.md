# Report
1. Completed the python program to convert Arabic Numerals to Roman Numerals and created a test python file.
2. Used `flake8` linter to check the coding style by GithubAction.
3. Used `pytest` to run the test python file by GithubAction.

## Committed files
- `arabic2roman.py`
This is the main program to solve the number converting problem.
I defined a ruction called `arabic2roman(num)`, the input `num` is arabic number ranges from 0 to 3999, and the fuctions will return the proper Roman number from `' '` to `'MMMCMXCIX'`. 
If input arabic number is bigger than 3999 then it will return `'Number too large.'`.

- `test_arabic2roman.py`
This is the test program for `arabic2roman.py`. The function `test_0()` will be automatically runned by `pytest` tool. Test cases includes 0 to 3999 and an exeption case 4000.

## Github Actions
### Continuous Build
- Linter
I used `flake8` as the linting tool to avoid merging code incompatible with project-supported configurations. The results can be found in GitHubAction.


### Continuous Build
- Test
I used `pytest` as the testing tool to do the black box test and unit test.
The results can be found in GitHubAction.


## Workflow
1. Proposed a new feature.
2. Create a new branch on git to develop the feature.
3. Complete code and commit to feature branch.
4. Ran CB (linter) on GitHub Action and revise the code until meet the linter requirements.
5. Ran CI (unit tests) by purest on GitHub Action and fixed spotted bugs.
6. Made a final review and ready to merge feature branch to stable branch.
7. Merged into master and completed feature development.

# Continuous-Integration
Objective of this exercise is to learn continuous build process (CB) and continuous integration (CI). 
You are expected to: 

- Write python program to convert Arabic Numerals to Roman Numerals 
- Integrate Continuous Build Process to check if your software in each development stage passed the build process. 
- Integrate unit test and run the unit test in continuous integration process.

For more informaiton, please check the assignment presentation.

Deadline for completion of this project is January 29th, 2019. 
You are expected to show all aspects of your work. This includes results of build process. 
You are expected to use Github actively during this exercise.
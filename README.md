# stackstorm.pack.template

The following template provides details how a new "StackStorm Pack" Gitlab project repository should be created. New repositories are generally created by the DevOps engineers, as some modifications are required to the repository settings. In the case of StackStorm Packs requests for new repositories should be directed to RAP Team leader. 

Developers should ensure that when creating new StackStorm Pack projects that the below repository directory structure and naming conventions are adhered too. 

## Useful Links 
For additional information about repository structure, branching, creating, committing or merging... please reference the below links. 

📖 [**Repository Structure**](TBC) |
📖 [**Guideline - Commits and Merge**](https://confluence.dimensiondata.com/display/STDA/Guidelines+for+code+commit+and+merge) |
📖 [**Offical Pack Documentation**](https://docs.stackstorm.com/packs.html) |

## How to use this repository?
The following section provides steps on how to use this repository to create additional StackStorm Packs. 

The below steps detail how to use this template:
1. Using your favorite IDE clone this template repository to your local machine.
2. Change directory to the newly clone repository making sure the branch is Master.
3. The template repository files should now be available on your local device. 
4. Delete the temp txt files from actions and tests directory. 
5. Create a new StackStorm Pack repository in the following location: https://scm.dimensiondata.com/AU-Automation/RAP/stackstorm-packs 
6. Clone the newly created pack to your local machine. 
7. Copy the below files from the template directly to the newly created StackStorm Pack directory. 
    * .gitlab-ci.yml 
    * pack.yml
8. Copy pack or action files from local stackstorm development folder into the newly created StackStorm pack directory. Once happy commit your code. 


### Pack / Project Naming Convention
When creating a new project based on this template, you should reference the following naming conventions: 

https://confluence.dimensiondata.com/display/GSCO/Naming+Convention

### Generating dimensiondata-info.json

https://code.dimensiondata.com/generator

### Creating a useful README file

https://confluence.dimensiondata.com/display/GSCO/README

### Pipeline Details (what does it do?)

When creating StackStorm packs it is important that testing be completed on a CI pipeline prior to deployment, adhering to this ensures that the pack will:

* Have a basic level of quality
* Should be free from errors
* Won't fail to install into StackStorm
* Be tested and have passed them during the testing phase
* Provide fast feed back on code commit
Test mod

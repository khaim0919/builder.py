__version__ = 'v0.0.2'

import pathlib
import os
import shutil
import time
import asyncio
import logging
import logging as log

# THIS WILL OVERWRITE IT EVERY TIME!!! TODO: FIX THIS LATER WITRH A DATETIME OR SOMETHING
log.basicConfig(level=logging.INFO, filename='builder.log', filemode='w', 
    format="[%(asctime)s]:%(levelname)s:%(message)s")

# debug
# info
# warning
# error
# critcal 
# in that order. 

# colours for console
percent     = '\033[90m'
addinfo     = '\033[90m'
warning     = '\033[93m'
build_error = '\033[91m'
success     = '\033[92m' 
fatal       = '\033[91m' 
impinfo     = '\033[97m'
body        = '\033[0m'

# variables for console output
# FILES_TO_DELETE = None
# FILES_TO_BUILD = None
# files_built = 0
# files_deleted = 0
# percent_complete = 0

# start_time = time.time_ns()

# //// BODY ///// 

def build_file(which: str): 
    pass

    # REQUIRED
    # process.get_metadata()
    # process.get_template()

    # Customise your markdown and extensions!
    process.basic_md()
    process.callouts()
    process.ids()
    process.logic()
    process.rich_tags()
    # process.document_tags()

    # add your extension calls here, and its contents in the process: class. 

    # you can also use this to customise your markdown for yoyure exact needs!!
    # we plan to cover
    # daring fireball md
    # kramdown
    # obsidan md
    # defintions
    # etc!

    log.info(f"{which} finished building!")


def get_partials(): 
    pass

def build_html_template(html_template): 
    get_partials() 

    ... 

def handle_logic(statement: str): 
    pass
    
    # any tags with %, like {{% if frontmater.author %}}
    # if it needs furhrter parsing without that, its an advanced variable. 
    # example: {{date:DD MMM YYYY}}

def process_manager(): 
    build_process()

    # when file returned: 
    #print(f'{success}{files_built}{addinfo}/{body}{files_to_build}{addinfo} {addinfo}({percent_complete}%){body} {child} {success} Finished Building{body}')

def build_process(): 

    build_file()

class process: 

    def basic_md(): 
        pass

    def callouts(): 
        pass

    def ids(): 
        pass

    def logic(): 
        pass

    def rich_tags(): 
        pass


    # Paste extension functions here!

# ///////////////

# build_time = round((time.time_ns() - start_time) / 1000000000, 2)
# if build_time <= 0.1: 
#     build_time = 'LESS THAN 0.1 SECCONDS'
# else: 
#     build_time += ' SECCOND'

# # print the success and exit with a code of 0 (success)
# print(f'{success} --PROCESS FINISHED IN {build_time}-- {body}')
# exit(0) # 0 = success


Directories and Files
---------------------

## Pointers to documentation
* [Documentation in Sphinx](https://readthedocs.org/projects/webwork-adaptivehints/) (figure out how to build after making changes in github)
* [Architecture Diagram](https://docs.google.com/drawings/d/19nmZt2Dzaz0_3F8tUUwOE_SmPAN_-e9J-Xx3GqYPA24/edit) (Update and move to lucidchart which has better templates for block diagrams)

## Structure of this github
* README.md:    This file  
* setup.sh    A script for setting the environmental variables. Run _source setup.sh_ at root direcotry.
* `setup_mysql_dump.sh`     A script for setting up environment variables to point to a directory containing mysql dumps.  Run `source setup_mysql_dump.sh` as root
* src         **DIR** All of the code
* data        **DIR** All of the data

### ansible
* Ansible is a tool for provisioning/configuring development environments

### src
* README.md: A markdown file explaining how to use the student\_adaptive\_server
* active_labelling_server
* student_adaptive_server
* config.yaml
* notebooks:		Yoav's developing code, in ipython notebook format
* python:				Yoav's stable code
* piazza
* webwork

#### src/python
* ProcessRealtimeMysqlDump.py: input= directory containing dumps of realtime and 
    standard webwork tables  output= ProcessedLogs.pkl
* ProcessLogs.py: input= log file directory output= ProcessedLogs.pkl
* ProcessingErrors.txt: lines that failed to parse in the log files.
* ParsingPGfiles.py: Translate a directory with PG files into a pickle file (problemTexts.pkl) which contains the 
   text preceding each answer block.
* PlotTiming.py : Generates scatter plots of attempt times for a user and an Assignment.
* BehaviourAnalysis.py:   for each user and problem Compute the number of attempts, total time 
  and whether or not the correct answer was found, as well as all of the attempts themselves.
	input=ProcessedLogs.pkl, output=BehavioralStatistics.pkl
* reportStruggles.py Find problems on which many students had a hard time, and generate the
  data combining the PG information and the answer attempts.

### data
* OutputFiles:		Human readable files generated by the analysis scripts, includes files that are edited by the instructor
								to add hints in response to student struggles
* PickleFiles:		Machine readable tables, the wrangled version of the input source files.
* assignment3_analysis
* course_webwork_data : The webwork problem source files (.def and .pg files)
* cse103_original_data/WebWork/logs	: The logs data resides here
* dependency_diagram.svg
* notable_session_plots.html
* notable_session_plots.md
* problem_3_1_analysis
* session_attempt_times
* student_adaptive_server
* webwork_data_description.html
* webwork_data_description.md



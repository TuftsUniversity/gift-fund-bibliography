**Author:**           Henry Steele, Library Technology Services, Tufts University
**Name of Program:**  Citations
**Files:**			  citations.py, Scripts/functions.py
**Date created:**     2018-12

**Purpose:**
  - To create a series of word documents that contain bibliographies of all the Titles
	purchased in a given fiscal year for a given library (Tisch or Ginn)
  - This github repo is in the Tufts University github.com organization at https://github.com/TuftsUniversity/gift-fund-bibliography 
  

**Command:** 
  - install requirements (first time)
	  - python3 -m pip install -r requirements
  - run
	  - python3 citations.py
**Method:**
  - provide library and fiscal year prompt
  - program retrives the appropriate Analytics report:
	  - either/or
		  - /shared/Tufts University/Reports/Collections/Gift Funds/Titles Purchased with Gift Funds - Tisch - Generic for Script
		  - /shared/Tufts University/Reports/Collections/Gift Funds/Titles Purchased with Gift Funds - Ginn - Generic for Script
	  - outputs:
		  - MMS Id
		  - fund
	  - filters on
		  - "MMS Id is not equal to / is not in  -1"
		  - (Tisch) "AND Fund Ledger Code is equal to / is in  dalex; dalel; daron; dbarr; dcamp; dchri; dcros; dduke; dfitc; dgiff; dgonz; dgord; dhaly; dharo; dloeb; dmeas; dnewh; dpall; dprit; drose; drosg; dshap; dsper; dtisc; dwill; dfox; docon; dcohe; dargo; dblak; dmarc"
		  - OR (Ginn) "Fund Ledger Name is equal to / is in  Bradley - Books; Cabot - Books; Fares - Books; Hay - Books; Imlah - Books; Maney - Books; Raanan - Books; Salacuse - Books; Saskawa-NPP - Books"
		  - "AND Transaction Date is prompted"
			  - this is passed as a 'saw' XML filter in the URL that encodes the date range
  - retrieves the XML report, iterates through and parses MMS Id and fund
  - performs an SRU search by MMS Id
  - parses out relevant title, author, and pulication information field from bib XML
	  + MMS Id
	  + Main entry Author (MARC 100|a)
	  + Main entry Author relator (MARC 100|e)
	  + Second author (MARC 110|a)
	  + Second author relator (MARC 110|e)
	  + Corporate author (MARC 700|a)
	  + Corporate author relator (MARC 700|e)
	  + Second corporate author (MARC 710|a)
	  + Second corporate author relator (MARC 710|e)
	  + Title (MARC 245|a)
	  + Subtitle (MARC 245|b)
	  + Place of publication (MARC 260|a)
	  + Name of publisher (MARC 260|b)
	  + Date of publication (MARC 260|c)
	  + Place of second publication (MARC 264|a)
	  + Name of second publisher (MARC 264|b)
	  + Date of second publication (MARC 264|c)
  - turns this data into a ".bib" BibTex-style file
  - uses locally python-citeproc "pseudo LaTex" to create bibliography, and docx module to write these to Word


**Dependences:**
  - in "requirements.txt"
      + django<2
	  + pandas
	  + openpyxl
	  + tk
	  + numpy
	  + future
	  + lxml
	  + python-docx
	  + citeproc-py


**Output:**
  - "/Processing/*" directory contains intermediate ".bib" file, which is in BibTex that citeproc
  - "/Output/*" directory contains final Word .docx file
  
**Troubleshooting:**
  - The most likely errors you will encounter will be with encoding.  
	The script translates everythign into UTF-8 so foreign characters shouldn't be a problem,
	but if you do run into issues you may want to exempt the individual bib record from input files_to_ignore
	(in \/Processing), comment out the part of the code all the way up to where they are created, and rerun.
	Or fix the records and wait a day for a new Analtics report
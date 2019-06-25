**Author:**									Henry Steele, Library Technology Services, Tufts University

**Name of Program:**						Parse Funds

**Files:**									parseFunds.py, functions.py

**Date created:**							2018-12

**Purpose:**

- using parsed MARC exports from Alma and Analytics, create a make\_bibliography f titles purchased with a set of gift funds so libraries can send thank you letters to donors

**Method:**

- input a table containing all titles in the set of funds needing bibliographies for gift fund letters to donors
- parse these titles lists per fund to convert them to BibTex (LaTeX for bibliography)&quot;.bib&quot; format
- use Pybtex and a local system installation of Texworks latex processor, and create a latex file and output to PDF

**Input:**

- a tilde delimited text file containing a list of titles and funds with the following fields, from an exported MARC file from Alma.  This tabular file is created with the XSLT file in this directory &quot;giftFunds.xsl&quot; that takes a MARC XML export from Alma&#39;s Export Bibliographic Records job that was created from a managed set created by the &quot;Titles Purchased with Gift Funds - for Export&quot; at [https://analytics-na01.alma.exlibrisgroup.com/analytics/saw.dll?Answers&amp;path=%2Fshared%2FTufts%20University%2FReports%2FCollections%2FGift%20Funds%2FTitles%20Purchased%20with%20Gift%20Funds%20-%20for%20Export](https://analytics-na01.alma.exlibrisgroup.com/analytics/saw.dll?Answers&amp;path=%2Fshared%2FTufts%20University%2FReports%2FCollections%2FGift%20Funds%2FTitles%20Purchased%20with%20Gift%20Funds%20-%20for%20Export)

- Since fund data isn&#39;t reliably in bib records, this script also takes a Analytics fund report directly, from &quot;Titles Purchased with Gift Funds - MMS and Fund&quot; at [https://analytics-na01.alma.exlibrisgroup.com/analytics/saw.dll?Answers&amp;path=%2Fshared%2FTufts%20University%2FReports%2FCollections%2FGift%20Funds%2FTitles%20Purchased%20with%20Gift%20Funds%20-%20MMS%20and%20Fund](https://analytics-na01.alma.exlibrisgroup.com/analytics/saw.dll?Answers&amp;path=%2Fshared%2FTufts%20University%2FReports%2FCollections%2FGift%20Funds%2FTitles%20Purchased%20with%20Gift%20Funds%20-%20MMS%20and%20Fund)
- These are the fields needed for each Analytics report
  - &quot;Titles Purchased with Gift Funds - for Export&quot;:
  - MMS Id
  - Main entry Author (MARC 100|a)
  - Main entry Author relator (MARC 100|e)
  - Second author (MARC 110|a)
  - Second author relator (MARC 110|e)
  - Corporate author (MARC 700|a)
  - Corporate author relator (MARC 700|e)
  - Second corporate author (MARC 710|a)
  - Second corporate author relator (MARC 710|e)
  - Title (MARC 245|a)
  - Subtitle (MARC 245|b)
  - Place of publication (MARC 260|a)
  - Name of publisher (MARC 260|b)
  - Date of publication (MARC 260|c)
  - Place of second publication (MARC 264|a)
  - Name of second publisher (MARC 264|b)
  - Date of second publication (MARC 264|c)
  - Fund (MARC 981|a)
- &quot;Titles Purchased with Gift Funds - MMS and Fund&quot;
  - MMS ID (changed field name to &quot;MMS ID&quot; from &quot;MMS Id&quot;.  This is needed to match bib export)
  - Fund Ledger Name
  - Fund Ledger Code
- exclusion files
  - if you run this script and find that it hangs on certain funds, enter these fund names in the prompted exclusion list, and then run the LaTeX processes separately on these funds manually afterward

**Outputs:**

- A BibTex .bib file containing titles purchased with each fund in the input table
- a PDF of this data in human readable format suitable for attaching to a donor letter

**Dependences:**

- You need to have a working LaTeX processor on your computer.  I used this process with both MikTex and TexLive.  Installation instructions for MikTex and TexLive are below.  Note that because configuration of these various LaTeX utilities requires use of GUI Tools, I am not currently installing this on a server to which I only have command line accesss.

**Installation links:**

- https://miktex.org/howto/install-miktex
- https://www.tug.org/texlive/quickinstall.html

- Note that if you want Tex Live to take precedence, you have to list it first in the environment path variable.   You can see which program is used to process LaTeX by just typing &quot;latex -version&quot; in the command line You also need to add the &quot;biblatex&quot; and &quot;biblatex-biber&quot; packages through the MikTex admin console.

- Biber allows you more flexibilty with citations such as having both an author and translator or editors in the reference.  These directions are for MikTex but you could also manage this process using Tex Live.  Tufts Libraries want their citations in Chicago style, so you will also need to enable the
  - &quot;biblatex-chicago&quot; pacakage.

- These directions are for Windows.

-
  - open the MikTex admin console as an Administrator
  - go to Packages and choose &quot;biblatex&quot;
  - click the &quot;-&quot; sign to install (or update)
  - in packages, find miktex-biber-bin-x64.  Press &quot;-&quot; to install and/or update
  - in packages, find biblatex-chicago.  Press &quot;-&quot; to install and/or update
  - you must now update the changes in MikTex&#39;s database.
  - In the Tasks menu, click &quot;Refresh filename databases&quot;
  - Wait for this to finish.  It may take a minute or so.  A message with the status appears at the bottom of packages list.
  - In the Tasks menu, click Update package database
  - Wait for this to finish.  It may take a minute or so.  A message with the status appears at the bottom of packages list.

- Installation instructions for MikTex and TexLive are below.  Note that because configuration of these various LaTeX utilities requires use of GUI Tools, I am not currently installing this on a server to which I only have command line accesss.  Note that if you want Tex Live to take precedence, you have to list it first in the environment path variable.   You can see which program is used to process LaTeX by just typing &quot;latex version&quot; in the command line

- need to install a few modules:
  - pip install pandas

**Notes:**

- DOS vs. Linux
  - such as described at [https://stackoverflow.com/questions/3949161/no-such-file-or-directory-but-it-exists](https://stackoverflow.com/questions/3949161/no-such-file-or-directory-but-it-exists)
  - You can try converting the file to Unix format on linux by installing dos2unix.  See [https://unix.stackexchange.com/questions/277217/how-to-install-dos2unix-on-linux-without-root-access](https://unix.stackexchange.com/questions/277217/how-to-install-dos2unix-on-linux-without-root-access)
- character encoding of command prompt window
  - Note that some input files will contain Unicode that can&#39;t be parsed with command prompt&#39;s default ascii processor.  To get around this, follow the directions at [https://stackoverflow.com/questions/14109024/how-to-make-unicode-charset-in-cmd-exe-by-default](https://stackoverflow.com/questions/14109024/how-to-make-unicode-charset-in-cmd-exe-by-default) or simply Win - R \&gt; cmd /K chcp 1250 every time you run this script
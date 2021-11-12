STATs507
The repository is created for the course STATS 507 in the Universiry of Michigan.

In "stat507_ps2_q3.py", there are the code for analyzing the demographic datasets and  oral health and dentition datasets from the National Health and Nutrition Examination Survey NHANES. The code do the following data cleaning:
a.Use Python and Pandas to read and append the demographic datasets keeping only columns containing the unique ids (SEQN), age (RIDAGEYR), race and ethnicity (RIDRETH3), education (DMDEDUC2), and marital status (DMDMARTL), along with the following variables related to the survey weighting: (RIDSTATR, SDMVPSU, SDMVSTRA, WTMEC2YR, WTINT2YR). Add an additional column identifying to which cohort each case belongs. Rename the columns with literate variable names using all lower case and convert each column to an appropriate type. Finally, save the resulting data frame to a serialized “round-trip” format of your choosing (e.g. pickle, feather, or parquet).

b.Repeat part a for the oral health and dentition data (OHXDEN_*.XPT) retaining the following variables: SEQN, OHDDESTS, tooth counts (OHXxxTC), and coronal cavities (OHXxxCTC).

The local link for such README file is: 
https://mfile.umich.edu/?path=/afs/umich.edu/user/z/e/zeyuanli/507/github/README.md
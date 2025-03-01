# How to Chart Radiographics Top 10 Articles in a Google Spreadsheet

This guide will show you how to extract information from the Radiographics Top 10 Articles website and create a clean, organized Google Spreadsheet with details for every article. You will learn how to:

- Navigate to the Radiographics Top 10 Articles page
- Extract key details from each article (title, author list, DOI, year, residency year, level, abstract)
- Log into Google Drive and create a new folder and spreadsheet
- Configure dropdown menus and text formatting in the spreadsheet
- Clean and organize the data for later use in a Python program

Follow the steps below:

---

## Step 1: Open the Radiographics Website

1. Open your preferred web browser.
2. In the search bar, type **"Radiographics Top 10 Articles"**.
3. Look for a result labeled **"RG TEAM Top 10 Reading List"** and click it.

```
[SCREENSHOT_PLACEHOLDER]
Purpose: Shows a Google search result with "Radiographics Top 10 Articles" query
Content: The search results page with the RG TEAM Top 10 Reading List appearing as the top result
Value: Helps the user identify the correct search query and result to click
[/SCREENSHOT_PLACEHOLDER]

4. Once the page loads, you will see various categories (e.g., Breast Imaging, Cardiac) and highlighted articles for different residency years.

---

## Step 2: Navigate to a Specific Article Category

1. Identify a category you want to work with (for example, Breast Imaging).
2. Click on the desired category to open the list of articles associated with that residency year and level (Basic, Intermediate, Advanced).

```
[SCREENSHOT_PLACEHOLDER]
Purpose: Display a category page with a list of articles and residency year labels.
Content: Screenshot showing a category page with sections for R1 residents and sub-categories like Basic, Intermediate, etc.
Value: Helps the user recognize the website layout and where to locate article details.
[/SCREENSHOT_PLACEHOLDER]

3. Pick any article from the list to begin the extraction process.

---

## Step 3: Log into Google Drive and Create a New Folder

1. Open a new tab and navigate to [Drive.google.com](https://drive.google.com).
2. If you are not logged in, enter your Google account credentials. Note that the login process may vary:
   - Enter your email (e.g., pioruzroj at gmail.com) or the account you wish to use.
   - Complete the login process using your passkey or password as prompted.

```
[SCREENSHOT_PLACEHOLDER]
Purpose: Show the Google Drive login page and account selection prompt.
Content: The Google Drive login screen with fields for email and password or passkey, as applicable.
Value: Assists users in identifying the proper login interface.
[/SCREENSHOT_PLACEHOLDER]

3. Once logged in, create a new folder:
   - Click on **"New"** > **"Folder"**.
   - Name the folder **"rg-top10-articles"**.

```
[SCREENSHOT_PLACEHOLDER]
Purpose: Demonstrate folder creation in Google Drive.
Content: The Google Drive interface with the 'New Folder' dialog open and a sample folder name entered.
Value: Guides users on how to organize their files for this project.
[/SCREENSHOT_PLACEHOLDER]

---

## Step 4: Create a New Google Spreadsheet

1. In your newly created folder, click **"New"** > **"Google Sheets"** to create a blank spreadsheet.
2. Name the spreadsheet **"Top 10 Articles"**.

```
[SCREENSHOT_PLACEHOLDER]
Purpose: Show the creation of a new Google Sheet and renaming of the file.
Content: The Google Sheets interface within the new folder with the file renamed as "Top 10 Articles".
Value: Ensures users create and locate the correct file for data entry.
[/SCREENSHOT_PLACEHOLDER]

---

## Step 5: Set Up the Spreadsheet Layout

1. Open your Google Spreadsheet and prepare to enter data.
2. Create columns for the following data extracted from each article:
   - **Title**
   - **Author List**
   - **DOI** (Digital Object Identifier)
   - **Year**
   - **Residency Year (R Year)**
   - **Level**
   - **Abstract**

3. Optionally, adjust the spreadsheet to make it visually clean:
   - Wrap text in cells where necessary (except for the abstract if you prefer no wrapping).
   - Delete any extra rows or columns in the sheet.
   - Bold column titles for clarity.

```
[SCREENSHOT_PLACEHOLDER]
Purpose: Illustrate the spreadsheet header setup with defined columns.
Content: The Google Sheet showing the header row with columns labeled Title, Author List, DOI, Year, R Year, Level, and Abstract.
Value: Demonstrates the structure that will later house the extracted data.
[/SCREENSHOT_PLACEHOLDER]

---

## Step 6: Configure Dropdown Menus and Formatting

1. **Configure the "Level" Dropdown:**
   - Select the column intended for article levels.
   - Open **Data > Data validation** and set up a dropdown list with the following options: **Basic, Intermediate, Advanced**.
   - Optionally, assign colors to each level for easier visual reference.

2. **Configure the "R Year" Dropdown:**
   - Similarly, select the column for residency year (R Year).
   - Set up a dropdown with the options: **R1, R2, R3, R4**.
   - Use distinct or bold colors to highlight each residency year if desired.

```
[SCREENSHOT_PLACEHOLDER]
Purpose: Show how dropdown lists are configured in Google Sheets.
Content: The Data validation dialog in Google Sheets with a list of options for a dropdown being defined.
Value: Helps users replicate the dropdown configuration, ensuring consistency in data entry.
[/SCREENSHOT_PLACEHOLDER]

---

## Step 7: Extract and Enter Article Information

For each article listed on the Radiographics page, follow these steps:

1. **Open the Article Page:**
   - Click on an article from the category listing.
   - Note that you might not have access to the full article; this is acceptable for data charting.

2. **Extract Details:**
   - **Title:** Highlight the article title, copy it, and paste it into the corresponding cell in the spreadsheet.
   - **Author List:** Copy the author list. To remove extra spaces or formatting issues, paste the text into your browser's address bar first, then copy it and paste into the sheet.
   - **DOI:** Copy the DOI link. Pasting it directly into the spreadsheet should suffice.
   - **Year:** Determine the publication year (e.g., 2019) and enter it.
   - **Residency Year (R Year):** Based on the article’s listing (e.g., R1), select the appropriate option from the dropdown.
   - **Level:** Identify the level (Basic, Intermediate, or Advanced) from the article’s category and select it from the dropdown.
   - **Abstract:** Copy the abstract text. If the abstract contains extra line breaks or spaces, paste it into the browser’s address bar and then copy it to strip out unnecessary formatting before pasting it into the cell.

```
[SCREENSHOT_PLACEHOLDER]
Purpose: Show an example article page with highlighted text for the title, abstract, author list, and DOI.
Content: Screenshot of an article page with annotations (circles or arrows) indicating where the title, authors, DOI, and abstract are located.
Value: Provides users with a visual cue for identifying the elements to extract from the page.
[/SCREENSHOT_PLACEHOLDER]

3. **Clean Up the Data Entry:**
   - Ensure that text wrapping is enabled or disabled as needed (for example, turn off wrapping for the abstract if you want text to overflow cleanly).
   - Remove extra spaces manually by editing the cell if necessary, especially in the author list and abstract columns.

4. **Repeat:**
   - Continue this process for every article within the chosen category.
   - If there are multiple categories (for different residency years or topics like Cardiac), navigate back to the list and repeat the extraction process, ensuring each article is represented by one row in your spreadsheet.

---

## Step 8: Finalize and Beautify the Spreadsheet

1. Review your spreadsheet to ensure all articles have been entered correctly and consistently.
2. Delete any extra rows or unused columns to keep the sheet neat.
3. Optionally, format the titles in bold or apply other visual styles to improve readability.
4. Once finished, notify yourself (or your team) that the spreadsheet is ready for further processing (such as loading into a Python program).

```
[SCREENSHOT_PLACEHOLDER]
Purpose: Serve as a final overview of the completed Google Spreadsheet with all required data.
Content: Image of a clean, well-organized Google Sheet with article details entered, dropdown menus active, and proper formatting applied.
Value: Confirms the expected end result, making it easier for users to verify their work.
[/SCREENSHOT_PLACEHOLDER]

---

## Additional Tips

- When pasting text from the browser’s address bar, ensure no extra line breaks or spaces remain.
- Adjust text wrapping in Google Sheets as needed to maintain clarity without clutter.
- Be patient with data entry and double-check that every article is charted correctly before finalizing the spreadsheet.

---

By following these steps, you will have created a comprehensive and organized chart of Radiographics Top 10 Articles that can later be processed with your Python programs or other tools.

Happy charting!
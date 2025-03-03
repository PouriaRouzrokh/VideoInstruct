# How to Chart Radiographics Top 10 Articles into a Google Spreadsheet

This guide explains how to chart articles from the Radiographics Top 10 Reading List into a Google Spreadsheet. By following these steps, you’ll be able to extract and organize key details — including titles, authors, publication year, DOI, residency year, article level, and abstracts — from the Radiographics website. This neatly formatted spreadsheet can later be processed with Python or other automation tools.

> Note: The search result titled "RG TEAM Top 10 Reading List" is used as an example. Depending on your location and search history, the title may vary. Adjust accordingly if you do not see this exact title.

## Introduction

In this tutorial, you will:

- Navigate to the Radiographics Top 10 Articles page using a Google search.
- Select a category (e.g., Breast Imaging) and review the list of articles, divided by residency year and article level.
- Set up a dedicated Google Drive folder and create a Google Spreadsheet for recording article details.
- Extract article data such as title, author list, publication year, DOI (with error-checking), residency year, article level, and abstract. You'll use a plaintext extraction trick (pasting into the address bar) to remove unwanted formatting.
- Format the spreadsheet by creating dropdown menus for residency year and article level, and adjust text wrapping settings for clarity. You will learn how to both wrap text and revert to a single-line display for abstracts using the appropriate Google Sheets text wrapping options.
- Finalize the spreadsheet ensuring consistency, neat formatting, and error prevention.

Follow the detailed step-by-step instructions below.

## Step-by-Step Instructions

### 1. Access the Radiographics Top 10 Articles Page

1. Open your web browser.
2. In the address bar, search for "Radiographics Top 10 Articles".
3. From the Google Search results, locate and click on the link titled "RG TEAM Top 10 Reading List" (or a similar title if it varies).

```
[SCREENSHOT_PLACEHOLDER]
Purpose: Show the Google search results with "Radiographics Top 10 Articles" highlighted.
Content: A browser window displaying the search results with the top result titled "RG TEAM Top 10 Reading List" (or similar).
Value: Helps the user identify the correct search result and link to click.
[/SCREENSHOT_PLACEHOLDER]

```
4. After the page loads, observe multiple categories (e.g., Breast Imaging, Cardiac, etc.) with different residency years and paper levels (Basic, Intermediate, Advanced).

```
[SCREENSHOT_PLACEHOLDER]
Purpose: Display the Radiographics Top 10 Reading List page.
Content: The page with a visible list of categories, each showing various residency years and article levels.
Value: Assists in recognizing the consistent layout and navigation structure.
[/SCREENSHOT_PLACEHOLDER]

### 2. Select an Article Category

1. Click on one of the article categories (for example, Breast Imaging).
2. Scroll through the displayed list to review the articles. Notice that within each residency year (e.g., R1), there are subcategories like Basic, Intermediate, or Advanced.

```
[SCREENSHOT_PLACEHOLDER]
Purpose: Highlight an article category and its subdivisions.
Content: A section of the Radiographics page showing specific residency years and article levels within a category.
Value: Provides clarity on where to find and select the correct subset of articles.
[/SCREENSHOT_PLACEHOLDER]

### 3. Extract Article Information

For each article you wish to chart, extract the following details:

- **Title**: The article's title or topic.
- **Author List**: The names of the authors.
- **Year**: The publication year (e.g., 2019).
- **DOI**: A DOI link. **Verify** that the DOI link resolves correctly before recording. If it is invalid, malformed, or missing, either leave the cell blank or mark it as "N/A". You may also choose to format valid DOI links as hyperlinks using the =HYPERLINK() formula in Google Sheets if desired.
- **Residency Year (R Year)**: For example, R1, R2, etc.
- **Level**: The article level (e.g., Basic, Intermediate, Advanced).
- **Abstract**: A summary of the paper (optional but useful for further processing).

**Plaintext Extraction Tip for Copying Text (e.g., Abstract, Author List):**

1. Copy the desired text from the article's web page.
2. Paste the text into your browser’s address bar. This action removes any hidden formatting or special characters.
3. Copy the plain text from the address bar and then paste it into your spreadsheet cell.

```
[SCREENSHOT_PLACEHOLDER]
Purpose: Demonstrate the browser address bar trick for removing text formatting.
Content: A screenshot showing the process of pasting copied text into the browser's address bar and then re-copying the resulting plaintext.
Value: Illustrates a reliable method to extract clean text, ensuring consistency in your data.
[/SCREENSHOT_PLACEHOLDER]

### 4. Prepare Your Google Drive Workspace

1. Open a new browser tab and navigate to [Google Drive](https://drive.google.com).
2. Sign in to your Google account. If you need to use a different account, enter the appropriate email (e.g., pioruzroj@gmail.com) and follow the login steps.

```
[SCREENSHOT_PLACEHOLDER]
Purpose: Demonstrate signing in to Google Drive.
Content: Google Drive’s login page or main interface if already signed in.
Value: Guides the user in accessing their Google Drive account successfully.
[/SCREENSHOT_PLACEHOLDER]

3. Create a new folder:
   - Click the '+ New' button.
   - Select 'Folder'.
   - Name the folder (e.g., "rg-top10-articles").

```
[SCREENSHOT_PLACEHOLDER]
Purpose: Show folder creation in Google Drive.
Content: A screenshot of the Google Drive interface with the folder creation dialog open and the folder name entered.
Value: Helps ensure the user creates an appropriate workspace for organizing articles.
[/SCREENSHOT_PLACEHOLDER]

4. Open the new folder and create a new Google Spreadsheet:
   - Click '+ New' > 'Google Sheets'.
   - Name the spreadsheet (e.g., "Top10-Articles").

```
[SCREENSHOT_PLACEHOLDER]
Purpose: Display the newly created Google Spreadsheet in the folder.
Content: A screenshot of the Google Spreadsheet within the new folder, showing its title.
Value: Confirms that the user has correctly set up the workspace.
[/SCREENSHOT_PLACEHOLDER]

### 5. Set Up Your Spreadsheet

1. In your spreadsheet, add the following column headers in the top row:
   - Title
   - Author List
   - Year
   - DOI
   - R Year
   - Level
   - Abstract

2. Format the spreadsheet for readability and data consistency:
   - Remove any unnecessary default columns.
   - **Adjust Text Wrapping for Long Entries**:
     - To wrap text for longer entries (such as Abstracts that need to display in full): Select the cells or columns, then navigate to **Format > Text wrapping > Wrap**.
     - To keep abstracts in a single line, select the cells or columns, then choose **Format > Text wrapping > Overflow**.

```
[SCREENSHOT_PLACEHOLDER]
Purpose: Show text wrapping settings in Google Sheets.
Content: A screenshot of the Google Sheets interface highlighting the Format > Text wrapping menu with both 'Wrap' and 'Overflow' options, along with examples of text that is wrapped vs. in overflow mode.
Value: Provides visual proof to help users verify their formatting choices.
[/SCREENSHOT_PLACEHOLDER]

### 6. Create Dropdown Menus for Consistent Data Entry

1. **For the 'Level' Column:**
   - Click on the header of the Level column.
   - Go to **Data > Data validation**.
   - Under 'Criteria', select 'List of items' and enter: Basic,Intermediate,Advanced (separated by commas).
   - Optionally, assign background colors for each option to improve visual clarity.
   - Click **Save**.

2. **For the 'R Year' Column:**
   - Click on the header of the R Year column.
   - Go to **Data > Data validation**.
   - Under 'Criteria', select 'List of items' and enter: R1,R2,R3,R4.
   - Optionally, assign distinct colors as desired.
   - Click **Save**.

```
[SCREENSHOT_PLACEHOLDER]
Purpose: Illustrate setting up dropdown menus in Google Sheets.
Content: A screenshot of the Data Validation dialog box populated with a list of items for either the Level or R Year column.
Value: Ensures consistent data entry standards across the spreadsheet.
[/SCREENSHOT_PLACEHOLDER]

### 7. Populate the Spreadsheet with Article Data

For each article in your selected category, perform the following steps:

1. **Navigate to the Article Page:** Open the article page from the Radiographics website.

2. **Copy the Title:**
   - Copy the article title and paste it into the cell under the Title column.

3. **Copy the Author List:**
   - Copy the author list.
   - Use the plaintext extraction trick: Paste the copied text into your browser’s address bar, then re-copy the clean text, and paste it into the Author List cell.
   - This ensures removal of any extraneous formatting.

4. **Record the Year:**
   - Enter the publication year (e.g., 2019) into the Year column.

5. **Copy the DOI:**
   - Copy the DOI link from the page and paste it into the DOI column.
   - **Verify** that the DOI link resolves correctly. If it is invalid or missing, leave the cell blank or mark it as "N/A". Optionally, you can format a valid DOI as a hyperlink using the =HYPERLINK() formula.

6. **Set the Residency Year (R Year):**
   - Use the dropdown menu to select the appropriate residency year (e.g., R1).

7. **Set the Article Level:**
   - Use the dropdown menu to select the appropriate article level (e.g., Basic).

8. **Copy the Abstract:**
   - Copy the abstract text from the article.
   - Use the browser address bar technique (copy, paste into the address bar, copy again) to ensure you only obtain plain text without any hidden formatting.
   - Paste the clean abstract into the Abstract column. If you want to keep the abstract in a single line, be sure to set the text wrapping option to **Overflow** as described in Step 5.

```
[SCREENSHOT_PLACEHOLDER]
Purpose: Show a completely filled-out row in the spreadsheet for an article.
Content: A screenshot displaying one row with all columns (Title, Author List, Year, DOI, R Year, Level, Abstract) properly populated.
Value: Provides a clear example of the data entry process and how the final output should look.
[/SCREENSHOT_PLACEHOLDER]

Repeat these substeps for each article. For categories with multiple sections (e.g., Cardiac, Emergency), follow the same process to ensure uniform data entry.

### 8. Finalize and Tidy Up the Spreadsheet

1. Review the spreadsheet and delete any extra rows or columns that aren’t needed. This will ensure the sheet remains neat and visually appealing.
2. Enhance the appearance of the spreadsheet by formatting the headers (e.g., make them bold) and applying any additional style adjustments.
3. Confirm that all dropdown menus and text-wrapping settings are correctly applied.
4. Once complete, your spreadsheet should be fully prepared and ready for further processing in your Python project or other applications.

```
[SCREENSHOT_PLACEHOLDER]
Purpose: Show the final, clean spreadsheet interface.
Content: A screenshot of the completed Google Spreadsheet with properly filled rows, columns, dropdown menus, and formatted text (e.g., wrapped or overflow for abstract as chosen).
Value: Verifies that the spreadsheet is neat, consistently formatted, and ready for use.
[/SCREENSHOT_PLACEHOLDER]

### 9. Summary

You have now learned how to:

- Access and navigate the Radiographics Top 10 Articles website.
- Select an article category and extract essential metadata, using plaintext extraction to remove unwanted formatting.
- Set up a dedicated Google Drive workspace with a customized Google Spreadsheet.
- Create dropdown menus for uniform data entry in the spreadsheet for fields such as Residency Year and Article Level.
- Format text wrapping in Google Sheets to display long text appropriately or maintain single-line abstracts, as desired.
- Verify DOI links for correctness and handle missing or invalid DOIs properly.
- Finalize and tidy up the spreadsheet to ensure it is visually consistent and ready for further automated processing.

Happy charting!
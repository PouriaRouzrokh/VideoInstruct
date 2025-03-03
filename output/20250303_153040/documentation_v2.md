# How to Chart Radiographics Top 10 Articles into a Google Spreadsheet

This guide explains how to chart articles from the Radiographics Top 10 Reading List into a Google Spreadsheet. By following these steps, you’ll be able to extract key details such as titles, authors, publication year, DOI, residency year, article level, and abstracts from the Radiographics website and organize them in a neatly formatted Google Sheet that can later be processed with Python.

> Note: The search result titled "RG TEAM Top 10 Reading List" is used as an example. Depending on your location and search history, the title of the search result may vary. Adjust accordingly if you do not see this exact title.

## Introduction

In this tutorial, you will:

- Navigate to the Radiographics Top 10 Articles page using a Google search.
- Select a category (e.g., Breast Imaging) and review the list of articles, divided by residency year and article level.
- Open Google Drive, create a dedicated folder, and set up a Google Spreadsheet to record article details.
- Extract and paste article information such as title, author list, year, DOI, abstract, residency year, and level.
- Format the spreadsheet by adding dropdown menus for residency year and article level, and adjust text wrapping settings, ensuring consistency throughout.
- Prepare a neat and organized spreadsheet that is ready for further processing.

Follow the detailed step-by-step instructions below.

## Step-by-Step Instructions

### 1. Access the Radiographics Top 10 Articles Page

1. Open your web browser.
2. In the address bar, type a search query like "Radiographics Top 10 Articles".
3. From the Google search results, locate and click on the link titled "RG TEAM Top 10 Reading List" (or the equivalent if it varies in your region).

```
[SCREENSHOT_PLACEHOLDER]
Purpose: Show the Google search results with "Radiographics Top 10 Articles" highlighted.
Content: A browser window displaying a Google search with the top result being the "RG TEAM Top 10 Reading List" or similar title.
Value: Helps the user identify the correct search term and link to click.
[/SCREENSHOT_PLACEHOLDER]

```

4. Once the page loads, you will see multiple categories (e.g., Breast Imaging, Cardiac, etc.) along with various residency years and paper levels (Basic, Intermediate, Advanced).

```
[SCREENSHOT_PLACEHOLDER]
Purpose: Display the Radiographics Top 10 Reading List page.
Content: List of categories with several residency years and levels for each article.
Value: Assists in recognizing the layout and navigating the page effectively.
[/SCREENSHOT_PLACEHOLDER]

### 2. Select an Article Category

1. Click on one of the article categories (for example, Breast Imaging).
2. Scroll through the list to review the articles available. Notice that each residency year (e.g., R1) may contain several subcategories such as Basic, Intermediate, or Advanced.

```
[SCREENSHOT_PLACEHOLDER]
Purpose: Highlight an article category and its subdivisions.
Content: A section of the Radiographics page showing specific residency years and article levels.
Value: Provides clarity on where to find the correct subset of articles.
[/SCREENSHOT_PLACEHOLDER]

### 3. Extract Article Information

For each article you wish to chart, extract the following key details:

- **Title**: The topic or title of the article.
- **Author List**: Names of the authors.
- **Year**: The publication year (e.g., 2019).
- **DOI**: A DOI link. If an article lacks a DOI, leave the cell blank or mark it as "N/A".
- **Residency Year (R Year)**: For example, R1, R2, etc.
- **Level**: The article level, such as Basic, Intermediate, or Advanced.
- **Abstract**: A summary of the paper (optional but recommended for further processing).

**Tip:** When copying text (for example, the abstract or author list), use the following plaintext extraction trick to remove unwanted formatting:

1. **Copy** the text from the website.
2. **Paste** it into your browser’s address bar. This action strips any extra formatting or hidden characters.
3. **Copy** the cleaned text from the address bar, and then **paste** it into the appropriate cell in your spreadsheet.

```
[SCREENSHOT_PLACEHOLDER]
Purpose: Demonstrate the browser address bar trick for removing text formatting.
Content: A screenshot showing the process of pasting copied text into the browser's address bar and then copying the plain text again.
Value: Illustrates how to remove unnecessary formatting to avoid issues in your spreadsheet.
[/SCREENSHOT_PLACEHOLDER]

The reason for pasting into the address bar is that it converts the copied content into plain text, eliminating any embedded formatting or hidden characters that could interfere with data consistency.

### 4. Prepare Your Google Drive Workspace

1. Open a new browser tab and navigate to [Google Drive](https://drive.google.com).
2. Sign in to your Google account. If using a different account, type the appropriate email (e.g., pioruzroj@gmail.com) and follow the login prompts.

```
[SCREENSHOT_PLACEHOLDER]
Purpose: Demonstrate signing in to Google Drive.
Content: Google Drive login page or the main interface if already logged in.
Value: Guides the user in successfully accessing their Drive account.
[/SCREENSHOT_PLACEHOLDER]

3. Create a new folder:
   - Click the '+ New' button.
   - Select 'Folder'.
   - Name the folder (for example, "rg-top10-articles").

```
[SCREENSHOT_PLACEHOLDER]
Purpose: Show folder creation in Google Drive.
Content: A screenshot of the Google Drive interface with the folder creation dialog open and folder name entered.
Value: Helps verify that the user can correctly create a workspace for charting articles.
[/SCREENSHOT_PLACEHOLDER]

4. Open the new folder and create a new Google Spreadsheet:
   - Click '+ New' > 'Google Sheets'.
   - Name the spreadsheet (e.g., "Top10-Articles").

```
[SCREENSHOT_PLACEHOLDER]
Purpose: Display the newly created Google Spreadsheet in the folder.
Content: A screenshot of the Google Spreadsheet in the new folder with its title visible.
Value: Confirms that the user has correctly created the workspace.
[/SCREENSHOT_PLACEHOLDER]

### 5. Set Up Your Spreadsheet

1. In your spreadsheet, define the following column headers in the top row:
   - Title
   - Author List
   - Year
   - DOI
   - R Year
   - Level
   - Abstract

2. Format the spreadsheet for better clarity:
   - Remove any unnecessary columns that might be present by default.
   - **Set text wrapping**:
     - Select the cells or entire columns that might contain long text (e.g., Abstract).
     - Navigate to the menu: **Format > Text wrapping > Wrap**. If you prefer the abstract to remain in a single line, choose **Overflow** or **Clip** instead.

```
[SCREENSHOT_PLACEHOLDER]
Purpose: Show text wrapping settings in Google Sheets.
Content: A screenshot of the Google Sheets interface highlighting the Format > Text wrapping menu with the 'Wrap' option selected.
Value: Helps users correctly apply text formatting to ensure readability or maintain single-line abstracts as needed.
[/SCREENSHOT_PLACEHOLDER]

### 6. Create Dropdown Menus for Consistent Data Entry

1. **For the 'Level' Column:**
   - Click on the header of the Level column.
   - Go to **Data > Data validation**.
   - Under 'Criteria', select 'List of items' and enter: Basic,Intermediate,Advanced (separated by commas).
   - Optionally, assign background colors for each option to enhance visual clarity.
   - Click **Save**.

2. **For the 'R Year' Column:**
   - Click on the header of the R Year column.
   - Go to **Data > Data validation**.
   - Select 'List of items' and enter the list of residency years (e.g., R1,R2,R3,R4).
   - Optionally, assign distinct colors as desired.
   - Click **Save**.

```
[SCREENSHOT_PLACEHOLDER]
Purpose: Illustrate the setup of dropdown menus in Google Sheets.
Content: A screenshot of the Data Validation dialog with the list of items for either Level or R Year column.
Value: Ensures the user can enforce standard data entry for each category.
[/SCREENSHOT_PLACEHOLDER]

### 7. Populate the Spreadsheet with Article Data

For each article in your selected category, perform the following actions:

1. Navigate to the article’s page.
2. **Copy the Title:**
   - Copy the article title and paste it into the appropriate cell under the Title column.

3. **Copy the Author List:**
   - Copy the author list from the page.
   - **Use the plaintext extraction trick**: Paste the copied text into your browser’s address bar, then copy the cleaned text and paste it into the Author List cell.
   - This step ensures that any hidden formatting is removed.

4. **Record the Year:**
   - Enter the publication year (e.g., 2019) into the Year column.

5. **Copy the DOI:**
   - Copy the DOI link from the page and paste it into the DOI column. If the DOI is missing, leave the cell blank or mark it as "N/A".

6. **Set the Residency Year (R Year):**
   - Use the dropdown menu to select the appropriate residency year (e.g., R1).

7. **Set the Article Level:**
   - Use the dropdown menu to select the correct article level (e.g., Basic).

8. **Copy the Abstract:**
   - Copy the abstract from the article page.
   - Use the browser address bar technique (copy, paste into the address bar, then copy again) to strip any extra formatting and hidden characters.
   - Paste the cleaned abstract into the Abstract column. If you prefer the abstract to be kept in a single line (without text wrapping), adjust the text wrapping settings as noted in Step 5.

```
[SCREENSHOT_PLACEHOLDER]
Purpose: Show a filled-out row in the spreadsheet for an article.
Content: A screenshot displaying one complete row with columns for Title, Author List, Year, DOI, R Year, Level, and Abstract fully populated.
Value: Provides a clear example of data entry and formatting that ensures consistency and cleanliness in the spreadsheet.
[/SCREENSHOT_PLACEHOLDER]

Repeat the above process for each article in the category. If there are multiple categories (e.g., Cardiac, Emergency, etc.), repeat the extraction and data entry steps for each.

### 8. Finalize and Tidy Up the Spreadsheet

1. Review your spreadsheet and delete any extra rows or columns that are not required. This keeps the sheet neat and visually appealing.
2. Optionally, enhance the appearance by formatting the headers (e.g., making them bold) or applying other cell styles.
3. Once completed, you will have a clean, organized spreadsheet ready for further processing in your Python project or any other application.

```
[SCREENSHOT_PLACEHOLDER]
Purpose: Show the final, clean spreadsheet interface.
Content: A screenshot of the completed Google Spreadsheet with properly filled rows, columns, and visible dropdowns, along with neat formatting.
Value: Verifies that the user’s spreadsheet is complete and visually well-organized.
[/SCREENSHOT_PLACEHOLDER]

### 9. Summary

You have now learned how to:

- Locate and navigate the Radiographics Top 10 Articles website.
- Select the appropriate article category and extract key metadata using a plaintext extraction trick to remove unwanted formatting.
- Use Google Drive and Google Sheets to record extracted data, including title, author list, year, DOI, residency year, level, and abstract.
- Use Data Validation to create dropdown menus for standardized data entry.
- Format text wrapping in Google Sheets to ensure clarity or maintain single-line abstracts, according to your preference.
- Finalize the spreadsheet by tidying up unnecessary rows and columns, ensuring it is ready for subsequent automated processing.

Happy charting!
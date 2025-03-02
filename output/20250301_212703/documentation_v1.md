# Step-by-Step Guide: Charting Radiographics Top 10 Articles in Google Sheets

## Introduction

This guide demonstrates how to extract article information from the Radiographics Top 10 Reading List and organize it into a well-structured Google Sheets spreadsheet. The process involves:

- Visiting the Radiographics website
- Navigating through article categories
- Logging into Google Drive and creating a dedicated folder and spreadsheet
- Extracting key details from each article (title, author list, DOI, year, residency year, level, and abstract)
- Formatting and cleaning the data for further use in your Python projects or other applications

Follow the steps below to recreate this process automatically for all articles.

---

## Steps

### 1. Open the Radiographics Top 10 Articles Page

1. Open your web browser.
2. In the address bar, type `radiographics top 10 articles` and press Enter.
3. In the Google search results, click on the link labeled **RG TEAM Top 10 Reading List**.

```
[SCREENSHOT_PLACEHOLDER]
Purpose: Display the Google search results with the 'RG TEAM Top 10 Reading List' as the first result.
Content: A screenshot showing the browser window with the search query and the first result highlighted.
Value: Helps users recognize the correct search result to click on.
[/SCREENSHOT_PLACEHOLDER]
```

### 2. Explore the Article Categories

1. Once the Radiographics page loads, you will see various article categories (e.g., Breast Imaging, Cardiac, etc.) grouped by residency years and article levels (Basic, Intermediate, Advanced).
2. Click on any of these categories (for example, **Breast Imaging**) to view the articles available for that section.
3. Observe that each residency year (R1, R2, etc.) further classifies articles by level.

```
[SCREENSHOT_PLACEHOLDER]
Purpose: Show the Radiographics Top 10 Reading List page with visible article categories and residency classifications.
Content: A screenshot of the webpage with categories and different residency years clearly labeled.
Value: Assists users in quickly locating the section they need to work with.
[/SCREENSHOT_PLACEHOLDER]
```

### 3. Log into Google Drive

1. Open a new browser tab and go to [https://drive.google.com](https://drive.google.com).
2. If you are not already logged in, use your credentials to log in.
   - **Note:** Depending on your configuration, you might need to use a different account or a passkey if prompted. For example, you may see a "Choose an account" screen. Enter the required email address (e.g., `pioruzroj@gmail.com`) and any necessary passcodes or follow the login instructions provided by Google.

```
[SCREENSHOT_PLACEHOLDER]
Purpose: Demonstrate the Google Drive login screen.
Content: A screenshot showing the Google Drive login page with the account selection process.
Value: Helps users know what login screen to expect and how to proceed with signing in.
[/SCREENSHOT_PLACEHOLDER]
```

### 4. Create a New Folder and Google Sheets Spreadsheet

1. In Google Drive, click on the **New** button and select **Folder**.
2. Name the folder (e.g., `RG-Top10-Articles`) and create it.
3. Open the newly created folder by double-clicking it.
4. Inside this folder, click on **New** again and select **Google Sheets** to create a blank spreadsheet.
5. Name the spreadsheet (e.g., `Top 10 Articles`).

```
[SCREENSHOT_PLACEHOLDER]
Purpose: Show how to create and name a new folder and spreadsheet in Google Drive.
Content: A screenshot of Google Drive with the new folder creation dialog and a new Google Sheets document open inside the folder.
Value: Visual guidance on navigating Google Drive to set up your working directory.
[/SCREENSHOT_PLACEHOLDER]
```

### 5. Set Up Your Spreadsheet Columns

1. In your new Google Sheets document, create the following column headers in the first row:
   - Title
   - Author List
   - DOI
   - Year
   - R Year
   - Level
   - Abstract
2. Format the headers by bolding them for clarity.
3. For the **R Year** column, create a drop-down menu containing: `R1`, `R2`, `R3`, and `R4`.
4. For the **Level** column, create a drop-down menu with options such as `Basic`, `Intermediate`, and `Advanced`.
5. Optionally, apply color coding to the drop-down selections for visual distinction.

```
[SCREENSHOT_PLACEHOLDER]
Purpose: Illustrate a sample Google Sheet with the correct columns, drop-down menus, and formatting.
Content: A screenshot of the spreadsheet with column headers set and drop-down options for R Year and Level visible.
Value: Helps users verify that their spreadsheet is setup properly before data entry begins.
[/SCREENSHOT_PLACEHOLDER]
```

### 6. Extract and Enter Article Information

For each article in the selected category, perform the following steps:

#### a. Extract the Article Title

1. Navigate to the article detail page from the Radiographics website.
2. Highlight and copy the title of the article.
3. Paste the title into the corresponding cell in the **Title** column of your spreadsheet.

#### b. Copy the Author List

1. Highlight the author list from the article page.
2. **Tip:** To remove extra spaces or unwanted line breaks, paste the text into your browser’s address bar first, then copy it again before pasting it into the **Author List** cell.

#### c. Extract the DOI

1. Locate the DOI link on the article page.
2. Copy the DOI (as a URL).
3. Paste it into the **DOI** column cell for that article.

#### d. Enter the Year

1. Identify the article's publication year from the page (e.g., `2019`).
2. Type the year into the **Year** column cell.

#### e. Set the Residency Year and Level

1. Determine the residency year for which the article is intended (e.g., `R1`).
2. Select the appropriate option from the R Year drop-down menu.
3. Identify the article level (e.g., `Basic`, `Intermediate`, or `Advanced`).
4. Select the correct level from the Level drop-down menu.

#### f. Extract the Abstract

1. Highlight the abstract text from the article page and copy it.
2. To clean the text from any extra line breaks or spaces, paste the abstract into your browser’s address bar and copy it again.
3. Paste the cleaned abstract into the **Abstract** column cell for that article.

```
[SCREENSHOT_PLACEHOLDER]
Purpose: Show a split-screen view with the article webpage on one side and the Google Sheets spreadsheet on the other.
Content: A screenshot demonstrating how data (e.g., title, author list, DOI, year, R Year, Level, abstract) is entered into the spreadsheet.
Value: Provides visual confirmation of where and how to paste each piece of data.
[/SCREENSHOT_PLACEHOLDER]
```

### 7. Repeat the Data Extraction Process

1. Return to the Radiographics Top 10 Reading List.
2. Repeat the extraction steps (Section 6) for each article across various categories and residency years.
3. Delete any extra rows that may have been added if you end up with more rows than necessary.

### 8. Finalize and Beautify Your Spreadsheet

1. Review the entire spreadsheet to ensure all data is consistent, well-formatted, and cleansed of unnecessary spaces or characters.
2. Adjust column widths and apply any additional formatting (e.g., bolding titles) to improve the visual appeal.

```
[SCREENSHOT_PLACEHOLDER]
Purpose: Display the final cleaned and formatted spreadsheet.
Content: A screenshot of the completed Google Sheet with all articles entered, clean formatting, and customized drop-down menus.
Value: Ensures users can verify their work against an expected final product.
[/SCREENSHOT_PLACEHOLDER]
```

### 9. Completion Notification

1. Once all articles are entered and the spreadsheet is finalized, notify the end user that their Google Sheets file is ready to be used.
2. Save any changes made to the spreadsheet and share it with relevant stakeholders if needed.

---

## Questions or Clarifications

If any of the following details are unclear, please consider these questions:

- Do you require any additional columns beyond those mentioned (Title, Author List, DOI, Year, R Year, Level, Abstract)?
- Are there any specific formatting details (e.g., specific colors for drop-down menus) that need to be applied?
- Should the guide include any automated methods (e.g., scripts) to streamline any of the data entry processes?

This concludes the step-by-step guide.
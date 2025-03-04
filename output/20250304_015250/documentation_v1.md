# How to Chart Radiographics Top 10 Articles in Google Sheets

This guide explains how to automatically chart articles from Radiographics’ Top 10 Reading List into a structured Google Sheet. By following these steps, you will extract information such as the title, author list, DOI, year, resident year (R Year), level, and abstract for each article and organize it for further processing (e.g., with Python programs).

---

## Introduction

In this tutorial, you will learn how to:

- Navigate to the Radiographics Top 10 articles page via a Google search
- Select a category (e.g., Breast Imaging) to access the list of articles
- Log in to Google Drive and set up a new folder for the project
- Create a new Google Sheet, format columns, and add dropdown menus
- Extract article details (title, author list, abstract, DOI, year, resident year, and level) and populate the spreadsheet
- Clean up the data by removing extra formatting or characters

Follow the step-by-step instructions below.

---

## Step-by-Step Instructions

### 1. Navigate to the Radiographics Top 10 Articles Page

1. Open your web browser and go to your preferred search engine.
2. Type "Radiographics top 10 articles" in the search bar.
3. Look for the link labeled **RG TEAM Top 10 Reading List** and click it.

```
[SCREENSHOT_PLACEHOLDER]
Name: Search Results
Purpose: Show the Google search results displaying the RG TEAM Top 10 Reading List
Content: A web browser with the search results for "Radiographics top 10 articles" highlighting the correct link
Value: Helps users identify which search result to select
[/SCREENSHOT_PLACEHOLDER]

### 2. Explore the Radiographics Website

1. Once the page loads, you will see different categories (e.g., Breast Imaging, Cardiac, Emergency, etc.).
2. Choose any category (e.g., click on "Breast Imaging") to view articles organized by residency years and article levels (Basic, Intermediate, Advanced).

```
[SCREENSHOT_PLACEHOLDER]
Name: Radiographics Categories
Purpose: Display the Radiographics website with the available article categories
Content: A screenshot showing the page header, category names, and subcategories by residency year
Value: Provides clarity on the website layout and available categories
[/SCREENSHOT_PLACEHOLDER]

### 3. Set Up Google Drive and Log In

1. Open a new browser tab and navigate to `https://drive.google.com`.
2. If you are not already logged in, sign in using your Google account. Note: Some users may see a login prompt asking for a passkey or password.
   - For the example in the video, the email used is `pioruzroj@gmail.com`. Use your own credentials if different.

```
[SCREENSHOT_PLACEHOLDER]
Name: Google Drive Login
Purpose: Show the Google Drive sign-in screen
Content: A screenshot of the Google Drive login page with the email/password prompt
Value: Assists users in correctly signing in to their Google accounts
[/SCREENSHOT_PLACEHOLDER]

### 4. Create a New Folder in Google Drive

1. In your Google Drive main view, click the **New** button (usually on the upper left).
2. Select **Folder** from the dropdown menu.
3. Name the folder (e.g., `RG-Top10-Articles`) and click **Create**.

```
[SCREENSHOT_PLACEHOLDER]
Name: New Folder
Purpose: Display the process of creating a new folder in Google Drive
Content: A screenshot showing the New button dropdown with the Folder option, and the prompt to name the folder
Value: Guides users through organizing their files by creating a dedicated folder
[/SCREENSHOT_PLACEHOLDER]

### 5. Create a New Google Sheet

1. Open the folder you just created by double-clicking it.
2. Click the **New** button inside the folder and choose **Google Sheets** > **Blank spreadsheet**.
3. Once the new Google Sheet opens, rename it to `Top 10 articles` by clicking on the title.

```
[SCREENSHOT_PLACEHOLDER]
Name: New Spreadsheet
Purpose: Illustrate the creation and renaming of the Google Sheet
Content: A screenshot of the new blank Google Sheet with its title being edited
Value: Ensures the user correctly names and locates the document in their Google Drive
[/SCREENSHOT_PLACEHOLDER]

### 6. Set Up the Spreadsheet Columns

1. In the Google Sheet, create the following column headers:
   - **Title**
   - **Author List**
   - **DOI**
   - **Year**
   - **R Year** (Resident Year)
   - **Level**
   - **Abstract**

2. Adjust the column layout if necessary (e.g., delete unnecessary columns, resize columns).

```
[SCREENSHOT_PLACEHOLDER]
Name: Spreadsheet Headers
Purpose: Show the spreadsheet with column headers in place
Content: A screenshot of the Google Sheet with columns titled as instructed
Value: Provides a visual reference for proper column setup
[/SCREENSHOT_PLACEHOLDER]

### 7. Format Dropdown Menus and Apply Colors

1. **For Resident Year (R Year):**
   - Create a dropdown menu with the options: `R1`, `R2`, `R3`, `R4`.
   - Optionally, apply distinct colors to each option to improve visual appearance.

2. **For Level:**
   - Create a dropdown menu with the options: `Basic`, `Intermediate`, and `Advanced`.
   - Apply colors to these options if desired.

*Hint:* Use Google Sheets’ data validation feature to set up dropdowns.

```
[SCREENSHOT_PLACEHOLDER]
Name: Dropdown Setup
Purpose: Show the data validation dropdown menus setup for R Year and Level
Content: A screenshot of the Google Sheets data validation dialog with options pre-configured
Value: Assists users in setting up structured data entry with dropdown menus
[/SCREENSHOT_PLACEHOLDER]

### 8. Extract and Populate Article Data

For each article you wish to chart from the Radiographics page, perform the following steps:

1. **Copy the Article Title:**
   - Highlight the title of the article and copy it.
   - Paste the title into the **Title** column of the sheet.

2. **Extract the Author List:**
   - Highlight the author list on the article page and copy it.
   - To remove extra formatting, paste the text into your browser’s address bar, copy it again, and then paste it into the **Author List** column.

3. **Extract the Abstract:**
   - Highlight and copy the abstract from the article.
   - Use the same trick (paste into the address bar then copy again) to remove unnecessary line breaks or characters, then paste the clean text into the **Abstract** column.

4. **Copy the DOI:**
   - If the article shows a DOI link, copy the link directly and paste it into the **DOI** column.

5. **Enter the Year:**
   - Type the publication year (e.g., `2019`) into the **Year** column.

6. **Select from Dropdowns:**
   - Choose the appropriate Resident Year (e.g., `R1`) from the dropdown in the **R Year** column.
   - Choose the appropriate level (e.g., `Basic`, `Intermediate`, or `Advanced`) from the dropdown in the **Level** column.

*Example:* For an article in the Breast Imaging category for R1 residents at the Basic level, the row would include the title, cleaned author list, DOI, year (e.g., 2019), `R1` for Resident Year, `Basic` for level, and the abstract.

```
[SCREENSHOT_PLACEHOLDER]
Name: Data Entry Example
Purpose: Display an example of a populated row with properly formatted data
Content: A screenshot of a Google Sheet row with all sample data entered (Title, Author List, DOI, Year, R Year, Level, and Abstract)
Value: Helps users verify their data entry format and ensure consistency
[/SCREENSHOT_PLACEHOLDER]

### 9. Repeat for All Articles

1. Return to the Radiographics listing and use the same process for each article across all categories and residency years.
2. Remove any unwanted extra rows once all articles have been charted.
3. Optionally, format the sheet further (for example, bold the titles or adjust the colors to improve readability).

### 10. Finalize and Notify Completion

1. Review your Google Sheet to ensure all downloaded data is correctly entered and formatted.
2. When complete, save your changes. Your Google Spreadsheet is now ready to be used in your Python projects or further processing.
3. Optionally, notify any relevant users or teams that the file is complete.

```
[SCREENSHOT_PLACEHOLDER]
Name: Final Spreadsheet
Purpose: Show the completed Google Sheet with all articles charted
Content: A screenshot of the fully populated and formatted Google Sheet
Value: Provides a visual confirmation of the expected final product
[/SCREENSHOT_PLACEHOLDER]

---

## Conclusion

Following these steps allows you to efficiently extract and organize Radiographics’ top articles into a Google Sheet for further analysis or use in automated processes. By adhering to a systematic approach, you minimize data entry errors and ensure a consistent format for all articles.

Happy charting!
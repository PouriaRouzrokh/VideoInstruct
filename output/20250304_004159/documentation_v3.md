# Charting Radiographics Top 10 Articles into a Google Spreadsheet

This guide explains how to automatically chart articles from the Radiographics Top 10 Reading List into a Google Spreadsheet. You will learn how to navigate the Radiographics website, locate key article details (including DOI and publication year), determine the correct Residency Year and Level from the page structure, and organize the information in a well-formatted Google Sheet for further processing.

---

## Table of Contents

1. [Access the Radiographics Website](#1-access-the-radiographics-website)
2. [Select a Category and Article](#2-select-a-category-and-article)
3. [Log In to Google Drive](#3-log-in-to-google-drive)
4. [Create a New Folder and Spreadsheet](#4-create-a-new-folder-and-spreadsheet)
5. [Set Up Your Spreadsheet](#5-set-up-your-spreadsheet)
6. [Extract and Enter Article Data](#6-extract-and-enter-article-data)
7. [Finalize Your Spreadsheet](#7-finalize-your-spreadsheet)

---

## 1. Access the Radiographics Website

1. Open your web browser.
2. In the search bar, type **"Radiographics top 10 articles"**.
3. In the Google search results, click on the link labeled **"RG Team Top 10 Reading List"**. This page lists various article categories organized by residency years and article level.

```
[SCREENSHOT_PLACEHOLDER]
Name: radiographics search
Purpose: To show the Google search results for "Radiographics top 10 articles".
Content: A browser window displaying a Google search result page with the "RG Team Top 10 Reading List" link highlighted.
Value: Assists users in confirming they have accessed the correct Radiographics page.
[/SCREENSHOT_PLACEHOLDER]
```

---

## 2. Select a Category and Article

1. On the Radiographics page, several article categories will be visible (e.g., Breast Imaging, Cardiac, etc.), with subdivisions by residency year and article level. These subdivisions indicate the Residency Year (e.g., R1 for first-year residents) and the Level (Basic, Intermediate, Advanced) of the article.
2. Click on a desired category (for example, **"Breast Imaging"**). This will display a list of articles for a specific residency year (e.g., R1) and indicate the article level (e.g., Basic). Use these cues to determine the appropriate Residency Year and Level for data entry later on. For instance, if an article is grouped under R1 and labeled as Basic, then later in the spreadsheet, you will select "R1" for Residency Year and "Basic" for Level.
3. Click on any article from the list. The full link may not be available, but the visible metadata (title, DOI, publication date, abstract) is sufficient for charting.

```
[SCREENSHOT_PLACEHOLDER]
Name: category selection
Purpose: Display the Radiographics page with categories, residency year, and level indicators.
Content: The Radiographics Top 10 Reading List showing labeled sections for residency years (e.g., R1) and levels (e.g., Basic), with a selected category highlighted.
Value: Helps users identify how to determine Residency Year and Level from the page structure.
[/SCREENSHOT_PLACEHOLDER]
```

---

## 3. Log In to Google Drive

1. Open a new browser tab and navigate to [https://drive.google.com](https://drive.google.com).
2. Log in to your Google account. If you're not already signed in or need to use a different account, select the appropriate account and enter your login credentials or passkey when prompted.

```
[SCREENSHOT_PLACEHOLDER]
Name: drive login
Purpose: Demonstrate the Google Drive login process.
Content: A browser displaying the account selection or Google Drive dashboard after login.
Value: Confirms users have successfully logged in to Google Drive to access and create files.
[/SCREENSHOT_PLACEHOLDER]
```

---

## 4. Create a New Folder and Spreadsheet

1. In Google Drive, click on the **New** button and select **Folder**.
2. Name the folder **"rg-top10-articles"** and create it.
3. Open the newly created folder.
4. Inside the folder, click on the **New** button again and select **Google Sheets** to create a new, blank spreadsheet.
5. Name the spreadsheet **"top10-articles"**.

```
[SCREENSHOT_PLACEHOLDER]
Name: new folder
Purpose: Demonstrate creating a new folder in Google Drive.
Content: The process of creating a folder named "rg-top10-articles" in Google Drive.
Value: Helps users organize their files before starting data entry.
[/SCREENSHOT_PLACEHOLDER]

[SCREENSHOT_PLACEHOLDER]
Name: new spreadsheet
Purpose: Illustrate the creation and naming of a new Google Sheet.
Content: A browser view showing the newly created Google Spreadsheet titled "top10-articles" inside the folder.
Value: Confirms that the workspace has been set up correctly.
[/SCREENSHOT_PLACEHOLDER]
```

---

## 5. Set Up Your Spreadsheet

Set up your spreadsheet with clear, consistent headers. Create the following columns:

- Title
- Author List
- DOI
- Publication Year
- Residency Year (with a drop-down: R1, R2, R3, R4)
- Level (with a drop-down: Basic, Intermediate, Advanced)
- Abstract

1. In the header row, enter the columns exactly as listed above so that later data entry remains consistent.
2. Configure drop-down menus for the **Residency Year** and **Level** columns:
   - For Residency Year, add options: R1, R2, R3, R4.
   - For Level, add options: Basic, Intermediate, Advanced.
3. Apply formatting to enhance readability by bolding the header row and, if desired, applying colors to flow selections.

```
[SCREENSHOT_PLACEHOLDER]
Name: spreadsheet setup
Purpose: Display the header setup and drop-down configuration in Google Sheets.
Content: A Google Sheet showing a header row with columns: Title, Author List, DOI, Publication Year, Residency Year, Level, and Abstract. Drop-down menus are visible in select cells.
Value: Provides a visual guide to structuring the data entry sheet.
[/SCREENSHOT_PLACEHOLDER]
```

---

## 6. Extract and Enter Article Data

For each article, perform the following:

1. **Locate Article Details on the Radiographics Page:**
   - **Title & Author List:** Typically clearly visible at the top of the article's section.
   - **DOI & Publication Year:** These are usually found in the metadata section of the article, near the title or within a details subsection. Look for labels like "DOI:" or a publication date (e.g., "Published 2019").
   - **Abstract:** Copy the abstract text provided on the page.

2. **Clean Up the Abstract Text if Needed:**
   If the abstract text includes extra line breaks or unwanted spacing:
   - Copy the abstract text from the article page.
   - Paste it into a plain text editor (e.g., Notepad for Windows or TextEdit for macOS set to plain text mode) to remove any formatting.
   - Copy the cleaned-up text from the text editor and paste it into the Abstract column in your spreadsheet.

```
[SCREENSHOT_PLACEHOLDER]
Name: abstract cleanup editor
Purpose: Show the abstract text before and after cleanup in a plain text editor.
Content: The left side shows the abstract text with extra line breaks/spaces; the right side shows the text after cleanup in a plain text editor.
Value: Demonstrates how to ensure the abstract text is clean and free of formatting issues before entering it into the spreadsheet.
[/SCREENSHOT_PLACEHOLDER]
```

3. **Determine Residency Year and Level:**
   - The article page's layout groups articles by residency year. For example, if an article is in the section labeled "R1", then the Residency Year is R1.
   - Similarly, the article's level is can be deduced by the category label (e.g., "Basic", "Intermediate", or "Advanced") indicated in the layout of the page.

4. **Enter Data into the Spreadsheet:**
   - Add a new row for the article.
   - Paste the Title, Author List, DOI, Publication Year, and cleaned Abstract into their respective columns.
   - Use the drop-down menus to select the appropriate Residency Year and Level based on the article page's grouping.

---

## 7. Finalize Your Spreadsheet

1. **Review Your Data:**
   - Check that each row corresponds to one article and that all fields are entered correctly.
   - Remove any extra or unused rows to keep the sheet neat.

2. **Adjust Cell Wrapping:**
   To ensure information is displayed clearly without unwanted breaks:
   - In Google Sheets, go to the menu: **Format > Wrapping** and select the option that best suits your layout (Overflow, Clip, or Wrap).

3. **Enhance Visual Formatting:**
   - Bold article titles or apply other formatting as desired to enhance readability.
   - Once all articles are entered and the layout is satisfactory, your spreadsheet is ready for further data processing (such as integrating with Python scripts).

---

## Conclusion

By following these steps, you have successfully extracted and charted the Radiographics Top 10 articles into a well-organized Google Spreadsheet. This guide clarified how to locate DOI and publication year information, determine Residency Year and Level from category groupings on the page, and clean up abstract text using a plain text editor. Finally, you learned how to adjust cell wrapping to ensure your data is presented clearly.

Happy charting!
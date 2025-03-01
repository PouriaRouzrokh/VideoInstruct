# Guide: Charting Radiographics Top 10 Articles into a Google Spreadsheet

This guide explains how to automatically chart articles from the Radiographics Top 10 Reading List into a Google Spreadsheet. You will learn how to access the Radiographics website, extract article information, sign in to Google Drive, create a new folder and spreadsheet, and set up the spreadsheet with proper formatting and data validation, including custom colors for dropdown menus as shown in the video.

---

## Introduction

In this task you will gather and record metadata for articles published on Radiographics’ Top 10 Reading List. The information you capture includes the title, author list, DOI, publication year, residency year (R1, R2, etc.), article level (Basic, Intermediate, Advanced), and abstract. This guide explains how to navigate the website, extract the required data, and format it correctly in a Google Sheets file that can later be loaded into a Python program or another application for further processing.

---

## Step-by-Step Instructions

### 1. Access the Radiographics Top 10 Articles Page

1. Open your preferred web browser.
2. In the search bar, type `radiographics top 10 articles` and press Enter.
3. Click the first search result titled **RG TEAM Top 10 Reading List**.
4. Verify that the page displays multiple categories of articles (e.g., Breast Imaging, Cardiac, etc.) sorted by residency years.

### 2. Select a Category and an Article

1. Choose a category (for example, Breast Imaging) by clicking on the category name.
2. The page will display articles for different residency years and paper levels (Basic, Intermediate, Advanced).
3. Click on one of the articles (for instance, an article under the Basic category for R1 residents) to view its details.

### 3. Prepare to Capture Article Details

Identify the following information to be recorded from the article's page:

- **Title**
- **Author List**
- **DOI** (copy the URL link directly)
- **Year** (e.g., 2019)
- **Residency Year** (e.g., R1, R2, R3, or R4)
- **Level** (e.g., Basic, Intermediate, or Advanced)
- **Abstract**

> Note: You may encounter page layouts that limit access to the full article text. This is acceptable as the goal is to chart the metadata.

### 4. Log into Your Google Drive

1. Open a new browser tab and navigate to [drive.google.com](https://drive.google.com).
2. If you are not logged in, or if a different account is active, sign out of any existing accounts.
3. Click **Use another account** and log in using your credentials. The login process may involve using a passkey or password, depending on your system.

### 5. Create a New Folder and Google Spreadsheet

1. In Google Drive, click the **New** button and select **Folder**.
2. Name the folder (for example, `RG-Top10-Articles`) and click **Create**.
3. Open the newly created folder by double-clicking it.
4. Inside the folder, click **New** again, then choose **Google Sheets > Blank spreadsheet**.
5. Rename the spreadsheet to a descriptive title, such as `Top 10 Article Picker` (click the document title at the top to rename it).

### 6. Set Up the Spreadsheet Column Headers

1. In the first row (Row 1), enter the following column headers:
   - **A1:** `Title`
   - **B1:** `Author List`
   - **C1:** `DOI`
   - **D1:** `Year`
   - **E1:** `R Year`
   - **F1:** `Level`
   - **G1:** `Abstract`
2. Adjust the column widths as needed.

### 7. Configure Data Validation and Apply Custom Colors to Dropdown Menus

#### Setting Up Dropdown for Article Level

1. Select the cells in the **Level** column (e.g., F2:F) where you will enter article levels.
2. Go to **Data > Data validation**.
3. Set the Criteria to **List of items** and enter: `Basic, Intermediate, Advanced`.
4. Save the data validation rule.
5. Now, assign colors for each option:
   - **Basic:** Apply a light pastel pink/peach color.
   - **Intermediate:** Apply a light or muted green color.
   - **Advanced:** Apply a light gray color.

   To do this, you can use **Conditional formatting**:
   - With the **Level** column selected, go to **Format > Conditional formatting**.
   - Create a rule for text exactly matching "Basic" and set the background color to the pastel pink/peach color.
   - Create a second rule for text exactly matching "Intermediate" and set the background color to the light/muted green.
   - Create a third rule for text exactly matching "Advanced" and set the background color to light gray.

#### Setting Up Dropdown for Residency Year

1. Select the cells in the **R Year** column (e.g., E2:E) where you will enter residency years.
2. Go to **Data > Data validation**.
3. Set the Criteria to **List of items** and enter: `R1, R2, R3, R4`.
4. Save the data validation rule.
5. Now, assign colors for each option using **Conditional formatting** in the same manner:
   - **R1:** Apply a dark blue background.
   - **R2:** Apply a dark red background.
   - **R3:** Apply a dark teal background.
   - **R4:** Apply a dark green background.

> Note: Since the video did not provide exact hexadecimal color codes, use the color descriptions as a guide to choose the closest available shades in Google Sheets.

### 8. Enter Article Data into the Spreadsheet

For each article in the chosen category, do the following:

1. Copy the **Title** from the article page and paste it into the `Title` column.
2. Copy the **Author List**. To remove extra spaces or formatting:
   - Paste the text into your browser’s address bar (or a plain text editor) and then re-copy it before pasting it into the spreadsheet.
3. For the **DOI**, copy the link URL directly and paste it into the respective cell.
4. Enter the **Year** (e.g., 2019) manually.
5. In the **R Year** column, use the dropdown menu to select the appropriate residency year (the cell will highlight with the assigned color, for example, dark blue for R1).
6. In the **Level** column, use the dropdown menu to select the article level (the cell will be colored accordingly: pastel pink/peach for Basic, light/muted green for Intermediate, or light gray for Advanced).
7. Copy the **Abstract** from the website. As with the author list, paste it into your browser’s address bar to remove extra formatting, then re-copy and paste it into the Abstract column.

Repeat these steps for every article listed under the current category. If needed, navigate back and repeat for other categories such as Cardiac or Emergency.

### 9. Finalize and Clean-Up

1. Review your spreadsheet to ensure all data is correctly entered and formatted:
   - Verify that all dropdown selections display the corresponding custom colors as described.
   - Remove any extra or unused rows to keep the spreadsheet clean.
   - Adjust any formatting (e.g., bold headers) to improve readability.

2. Once everything is set, notify yourself or your team that the Google Spreadsheet is complete and ready for integration with your Python project or other applications.

---

## Conclusion

By following this guide, you will have successfully compiled a detailed, well-formatted Google Spreadsheet containing all the metadata for Radiographics Top 10 Articles. With correctly configured dropdown menus and custom color formatting, the sheet will be both informative and visually appealing. Enjoy charting and further processing the data as needed!

Happy charting!
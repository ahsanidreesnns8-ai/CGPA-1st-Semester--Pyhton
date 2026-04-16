# CGPA-1st-Semester--Pyhton
This Project is for calculating CGPA that will facilitate the students.
# Simple GPA Calculator 📊

A dedicated Python utility designed to calculate a student's Grade Point Average (GPA) based on University-standard credit hour weightage. This project was developed during my **1st Semester** to simplify academic performance tracking.

## 🌟 Features

- **Interactive Setup:** Prompts the user to initiate the calculation and displays the standard grading scale.
- **Grading Dictionary:** Includes a comprehensive mapping of letter grades (A+ to F) to their respective grade points.
- **Weighted Calculations:** Handles subjects with different credit hour values (1, 2, or 3 credit hours) to ensure an accurate weighted average.
- **Dynamic Input:** Users can input specific subject names and their achieved grades.
- **Input Validation:** Features a `try-except` block to catch potential value errors during the input process.

## 🧮 How It Works

The script calculates the GPA using the following weighted formula:

$$GPA = \frac{\sum (\text{Grade Points} \times \text{Credit Hours})}{\text{Total Credit Hours}}$$

1. The user defines how many subjects of each credit hour type (3, 2, or 1) they took.
2. The program iterates through each subject to collect the grade.
3. It multiplies the grade point by the credit hours and sums them up.
4. Finally, it divides the sum by the total credit hours (default set to 16) to provide a formatted result.

## 🚀 Usage

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/gpa-calculator.git](https://github.com/your-username/gpa-calculator.git)

## Author
M. Ahsan Idrees

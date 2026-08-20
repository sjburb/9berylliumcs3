# Computational Thinking Exercise
## [Smart Vending Machine]
## Name: Samuel Jess B. Urbano
## Section: Beryllium
## Last Name: Urbano
## Date: 8/20/2026
---

## Step 1: Identify the Big Problem
### Main Problem
The machine has problems with payment, stock problems, button selection, and it's slow.
---
## Step 2: Identify the Sub-Problems
1. Incorrect change
2. Stock count unknown
3. Wrong items
4. Slow processing
---
## Step 3: Apply Computational Thinking Skills
| Sub-Problem | CT Skill | Proposed Solution |
|---|---|---|
| Incorrect change | Algorithm Design | Create a process to calculate proper change |
| Stock count unknown | Algorithm Design | Create an algorithm that detects when stocks of specific items are low |
| Wrong items | Decomposition | Breaks down vending machine processes |
| Slow processing | Algorithm Design | Create faster algorithms to make the machine run faster |
---
## Step 4: Algorithmic Solution
### Selected Sub-Problem
Incorrect change
### Pseudocode
START
Function Main
    
    Declare Integer Money
    Declare Integer Price
    Input Money
    Input Price
    If Money < Price
        Output "Done"
    Else
        Declare Integer Change

        Assign Change = Money - Price
        Output "Giving change.."
        Output "Your change is " & Change
    End
End

END
---

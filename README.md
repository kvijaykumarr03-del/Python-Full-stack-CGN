# 🐍 Python Full Stack & Relational Database Engineering

Welcome to the **Python Full Stack** repository! This repository contains comprehensive day-by-day training modules, code notes, and a production-grade relational database capstone project: the **Vehicle Rental System**.

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Database](https://img.shields.io/badge/Database-MySQL%20%7C%20SQLite-orange.svg)](https://www.mysql.com/)
[![Dataset](https://img.shields.io/badge/Verified%20Records-30%2C600-brightgreen.svg)](#-database-structure)
[![SQL Queries](https://img.shields.io/badge/SQL%20Queries-60%20(Simple%20%7C%20Medium%20%7C%20Hard)-purple.svg)](#-sql-analysis--60-practice-queries)

---

## 📑 Table of Contents

- [🌟 Featured Project: Vehicle Rental System](#-featured-project-vehicle-rental-system)
  - [🚀 Project Highlights](#-project-highlights)
  - [📌 Project Overview](#-project-overview)
  - [🔗 ER Diagram & Relationships](#-er-diagram--relationships)
  - [🎥 Project Demo & Screen Recording](#-project-demo--screen-recording)
  - [🗄️ Database Schema & Structure](#-database-schema--structure)
  - [📊 60 Graduated SQL Queries](#-60-graduated-sql-queries)
  - [🛠️ How to Run & Execute](#️-how-to-run--execute)
    - [Option 1: Interactive Python Runner (No MySQL Needed)](#option-1-interactive-python-runner-instant-sqlite)
    - [Option 2: MySQL Workbench / Command Line](#option-2-mysql-server-restoration)
  - [💼 Key Business Insights Explored](#-key-business-insights-explored)
  - [📁 Vehicle Rental System Files](#-vehicle-rental-system-directory-structure)
- [📚 Course Daily Curriculum Modules](#-course-daily-curriculum-modules)
- [👥 Contributing & License](#-author--details)

---

## 🌟 Featured Project: Vehicle Rental System

The **Vehicle Rental System** is an end-to-end, production-grade relational database and analytics project modeling the complete operational workflow of a modern commercial vehicle and car rental enterprise.

It demonstrates relational database modeling, referential integrity constraints, multi-table joins, grouped aggregations, nested subqueries, Common Table Expressions (CTEs), and window analytical functions across **30,600 verified records**.

---

### 🚀 Project Highlights

| Metric | Details |
|---|---|
| **Database** | `vehicle_rental_db` |
| **Entities / Tables** | 4 tables (`customers`, `vehicles`, `rental_locations`, `rentals`) |
| **Dataset Size** | **30,600 verified rows** |
| **SQL Practice Queries** | **60 queries** (20 Simple, 20 Medium, 20 Hard) |
| **Difficulty Progression** | Simple ➔ Medium ➔ Hard |
| **Zero-Setup Mode** | Interactive Python SQLite CLI runner (`run_project.py`) |
| **Tools Supported** | MySQL 8.0+, SQLite, MySQL Workbench, Python 3.x, DBeaver |

---

### 📌 Project Overview

The database models four interconnected commercial entities:

1. 👤 **`customers`** — Stores customer personal information, contact credentials, driving license identifiers, residency city, and account registration dates.
2. 🚘 **`vehicles`** — Fleet inventory management with vehicle model name, manufacturer brand, vehicle class/category (SUV, Sedan, Luxury, Electric, Compact SUV, Hatchback), fuel type, seating capacity, base daily rental rate, odometer mileage, and operational status.
3. 🏢 **`rental_locations`** — Commercial hubs, airport branches, downtown desks, and transit terminals across major metropolitan centers, with physical addresses and parking bay capacities.
4. 📋 **`rentals`** — The central transactional entity binding customers, vehicles, pickup stations, and drop-off stations. Records booking periods, trip duration in days, calculated bills, booking statuses (`Completed`, `Active`, `Cancelled`, `Reserved`), and payment methods (`UPI`, `Credit Card`, `Debit Card`, `Net Banking`, `Cash`).

---

### 🔗 ER Diagram & Relationships

<p align="center">
  <img src="Vehicle%20rental%20system/ER-Diagram.png" alt="Entity Relationship Diagram of the Vehicle Rental System" width="100%">
</p>

#### Entity Relationships & Cardinality:

```
customers (1) ──────────┐
                        │
vehicles (1) ───────────┼───< rentals (N)
                        │
rental_locations (1) ───┘  [pickup_location_id & return_location_id]
```

- **`customers` ➔ `rentals` (1 : N):** One customer can reserve multiple vehicle rentals over time.
- **`vehicles` ➔ `rentals` (1 : N):** One vehicle can be rented repeatedly across distinct scheduling windows.
- **`rental_locations` ➔ `rentals` (1 : N):** Each rental transaction originates at a pickup branch and terminates at a return branch (supporting one-way drop-offs).

---

### 🎥 Project Demo & Screen Recording

A full video walkthrough showcasing the project architecture, relational queries, and execution is included in the project folder:

<video src="Vehicle%20rental%20system/Screen%20Recording%202026-10-22%20235519.mp4" controls width="100%"></video>

> 📥 **Direct Video File:** [`Screen Recording 2026-10-22 235519.mp4`](Vehicle%20rental%20system/Screen%20Recording%202026-10-22%20235519.mp4)

---

### 🗄️ Database Schema & Structure

**Database Name:** `vehicle_rental_db`

#### Table Summary

| Table | Description | Records | Primary Key | Foreign Keys |
|---|---|---:|---|---|
| [`customers`](#1-customers-table) | Customer contact and driver license records | 10,000 | `customer_id` | — |
| [`vehicles`](#2-vehicles-table) | Fleet inventory, specifications, and daily rates | 500 | `vehicle_id` | — |
| [`rental_locations`](#3-rental_locations-table) | Pickup & return hubs, addresses, capacities | 100 | `location_id` | — |
| [`rentals`](#4-rentals-table) | Booking transactions, billing, and statuses | 20,000 | `rental_id` | `customer_id`, `vehicle_id`, `pickup_location_id`, `return_location_id` |
| **Total** | | **30,600** | | |

---

#### 1. `customers` Table
Stores customer profiles and license verifications.

| Column | Data Type | Constraint | Description |
|---|---|---|---|
| `customer_id` | `INT` | PRIMARY KEY | Unique customer identifier |
| `customer_name` | `VARCHAR(100)` | NOT NULL | Customer full name |
| `email` | `VARCHAR(100)` | NULL | Customer email address |
| `phone` | `VARCHAR(20)` | NULL | Contact phone number |
| `city` | `VARCHAR(50)` | NULL | Customer home city |
| `driver_license_no` | `VARCHAR(30)` | NULL | Government driving license number |
| `signup_date` | `DATE` | NULL | Customer account registration date |

---

#### 2. `vehicles` Table
Tracks fleet vehicles, pricing, and availability.

| Column | Data Type | Constraint | Description |
|---|---|---|---|
| `vehicle_id` | `INT` | PRIMARY KEY | Unique vehicle fleet identifier |
| `model_name` | `VARCHAR(100)` | NOT NULL | Model designation (e.g. Fortuner, Creta, Model 3) |
| `brand` | `VARCHAR(50)` | NOT NULL | Manufacturer (e.g. Toyota, BMW, Hyundai, Tesla) |
| `category` | `VARCHAR(30)` | NOT NULL | Class (SUV, Sedan, Luxury, Electric, etc.) |
| `fuel_type` | `VARCHAR(20)` | NOT NULL | Fuel type (Petrol, Diesel, Electric, Hybrid) |
| `seating_capacity` | `INT` | NOT NULL | Seating capacity (4, 5, 7 seats) |
| `daily_rate` | `DECIMAL(10,2)` | NOT NULL | Base rental rate per calendar day |
| `mileage_km` | `INT` | NULL | Cumulative odometer mileage in kilometers |
| `vehicle_status` | `VARCHAR(20)` | DEFAULT 'Available' | Availability (`Available`, `Rented`, `Maintenance`) |

---

#### 3. `rental_locations` Table
Physical branches and station hubs.

| Column | Data Type | Constraint | Description |
|---|---|---|---|
| `location_id` | `INT` | PRIMARY KEY | Unique station identifier |
| `location_name` | `VARCHAR(100)` | NOT NULL | Hub name (e.g. Airport Terminal Hub #1) |
| `city` | `VARCHAR(50)` | NOT NULL | Station city (e.g. Bangalore, Mumbai, Delhi) |
| `address` | `VARCHAR(150)` | NULL | Street address and local landmark |
| `contact_number` | `VARCHAR(20)` | NULL | Branch desk telephone number |
| `parking_capacity` | `INT` | NULL | Total vehicle bay capacity |

---

#### 4. `rentals` Table
Central transactional history and billing.

| Column | Data Type | Constraint | Description |
|---|---|---|---|
| `rental_id` | `INT` | PRIMARY KEY | Unique rental transaction identifier |
| `customer_id` | `INT` | FOREIGN KEY | References `customers(customer_id)` |
| `vehicle_id` | `INT` | FOREIGN KEY | References `vehicles(vehicle_id)` |
| `pickup_location_id` | `INT` | FOREIGN KEY | References `rental_locations(location_id)` |
| `return_location_id` | `INT` | FOREIGN KEY | References `rental_locations(location_id)` |
| `rental_start_date` | `DATETIME` | NOT NULL | Timestamp of vehicle pickup |
| `rental_end_date` | `DATETIME` | NOT NULL | Timestamp of vehicle drop-off |
| `rental_duration_days`| `INT` | NOT NULL | Duration of rental in days |
| `total_amount` | `DECIMAL(10,2)` | NOT NULL | Final invoice total |
| `rental_status` | `VARCHAR(20)` | NOT NULL | Status (`Completed`, `Active`, `Cancelled`, `Reserved`) |
| `payment_method` | `VARCHAR(30)` | NOT NULL | Method (`UPI`, `Credit Card`, `Debit Card`, `Net Banking`, `Cash`) |

---

### 📊 60 Graduated SQL Queries

The repository includes **60 hand-crafted, production-style SQL queries** categorized across three difficulty tiers:

#### 🟢 Simple Queries (Q1 – Q20) — [`Simple_queries.txt`](Vehicle%20rental%20system/Simple_queries.txt)
* **Skills Covered:** `SELECT`, `WHERE`, `LIKE`, `IN`, `ORDER BY`, `LIMIT`, `DISTINCT`, aggregate functions (`COUNT()`, `SUM()`, `AVG()`, `MIN()`, `MAX()`).
* **Example Topics:**
  - Filtering SUV vehicles and high-value rental rates (`> 3500.00`).
  - Active and completed rental status lookups.
  - Sorting top 10 highest-value rentals.
  - Overall customer base and total completed revenue summaries.

#### 🟡 Medium Queries (Q1 – Q20) — [`Medium_queries.txt`](Vehicle%20rental%20system/Medium_queries.txt)
* **Skills Covered:** `INNER JOIN`, multi-table 4-way relational joins, `LEFT JOIN` (unrented fleet discovery), `GROUP BY`, `HAVING`, `CASE` expressions, date functions (`YEAR()`, `MONTH()`).
* **Example Topics:**
  - Full trip itineraries resolving customer names, vehicle models, and pickup/return location stations.
  - Revenue aggregation grouped by vehicle manufacturer and vehicle category.
  - Identifying locations with high rental density (`HAVING COUNT(*) > 150`).
  - Analyzing customer spending tiers with `CASE` logic.

#### 🔴 Hard Queries (Q1 – Q20) — [`Hard_queries.txt`](Vehicle%20rental%20system/Hard_queries.txt)
* **Skills Covered:** Common Table Expressions (`WITH ... AS (...)`), window ranking functions (`ROW_NUMBER()`, `DENSE_RANK()`, `RANK()`), partitioned analytical queries (`PARTITION BY`), top-N queries, subqueries.
* **Example Topics:**
  - Ranking vehicles by completed revenue within each category using `DENSE_RANK()`.
  - Customers spending above the national average customer spend.
  - Top-N highest revenue models per city and manufacturer.
  - Percentage contribution of each vehicle category to overall gross sales.

---

### 🛠️ How to Run & Execute

#### Option 1: Interactive Python Runner (Instant SQLite)
You can test and execute all 60 queries instantly on macOS, Linux, or Windows without installing a MySQL server!

1. Open your terminal:
   ```bash
   cd "Vehicle rental system"
   ```
2. Run the interactive query engine:
   ```bash
   python3 run_project.py
   ```
3. Select which query suite to execute from the interactive menu:
   - `1` — Run Simple Queries (20 queries)
   - `2` — Run Medium Queries (20 queries)
   - `3` — Run Hard Queries (20 queries)
   - `4` — Run ALL 60 Queries sequentially
   - `5` — Reset / Rebuild SQLite database from master SQL dump

---

#### Option 2: MySQL Server Restoration

1. Open your terminal in the project directory:
   ```bash
   cd "Vehicle rental system"
   ```
2. Create the target database:
   ```sql
   CREATE DATABASE IF NOT EXISTS vehicle_rental_db;
   ```
3. Restore the complete master dump (DDL, constraints, and 30,600 verified records):
   ```bash
   mysql -u root -p vehicle_rental_db < vehicle_rental.sql
   ```
4. Verify table counts in MySQL:
   ```sql
   USE vehicle_rental_db;
   SELECT 'customers' AS tbl, COUNT(*) FROM customers
   UNION ALL
   SELECT 'vehicles', COUNT(*) FROM vehicles
   UNION ALL
   SELECT 'rental_locations', COUNT(*) FROM rental_locations
   UNION ALL
   SELECT 'rentals', COUNT(*) FROM rentals;
   ```

---

### 💼 Key Business Insights Explored

- **Top Revenue Vehicles:** Identified which vehicle models and manufacturers yield the highest gross revenue.
- **Customer Lifetime Value (LTV):** Segmented the top 5% repeat and highest-spending customers.
- **Hub & Branch Density:** Uncovered peak pickup locations to optimize fleet allocation across cities.
- **Category Profitability:** Compared profit margins and booking frequencies across SUVs, Luxury, Sedans, and Electric vehicles.
- **Fleet Idle Asset Detection:** Pinpointed zero-booking vehicles to minimize capital depreciation.

---

### 📁 Vehicle Rental System Directory Structure

```text
Vehicle rental system/
├── README.md                           # Comprehensive project documentation
├── Screen Recording 2026-10-22 235519.mp4 # Full HD project walkthrough & demo video
├── ER-Diagram.png                      # Entity Relationship Diagram
├── vehicle_rental.sql                  # Master MySQL database dump (30,600 rows)
├── vehicle_rental.db                   # Standalone SQLite database for zero-setup execution
├── run_project.py                      # Interactive Python query runner
├── Simple_queries.txt                  # 20 Beginner SQL practice queries
├── Medium_queries.txt                  # 20 Intermediate relational SQL queries
├── Hard_queries.txt                    # 20 Advanced SQL analytical queries (CTEs, Window Functions)
├── Database_Restore_Guide.txt          # Step-by-step restoration guide
└── Execution.txt                       # Query sequence and execution manual
```

---

## 📚 Course Daily Curriculum Modules

This repository also contains comprehensive curriculum study notes covering Python programming, data structures, algorithms, and full-stack development:

| Day | Module File | Topic Overview |
|---|---|---|
| **Day 1** | [`day1.txt`](day1.txt) | Python Fundamentals, Variables, Input/Output, Data Types |
| **Day 2** | [`Day-2.txt`](Day-2.txt) | Control Structures, Conditionals, Loops & Iteration |
| **Day 3** | [`day3.txt`](day3.txt) | Functions, Scope, Arguments, Return Values |
| **Day 4** | [`day4.txt`](day4.txt) | Strings, String Manipulation & Formatting |
| **Day 5** | [`day5.txt`](day5.txt) | Lists, Tuples, Sequences & Indexing |
| **Day 6** | [`day6.txt`](day6.txt) | Sets, Set Operations, Dictionaries & Mapping |
| **Day 7** | [`day7.txt`](day7.txt) | Advanced Data Structures & Comprehensions |
| **Day 8** | [`day8.txt`](day8.txt) | Object-Oriented Programming (OOP) — Classes & Objects |
| **Day 9** | [`day9.txt`](day9.txt) | OOP — Inheritance, Polymorphism, Encapsulation |
| **Day 10** | [`day10.txt`](day10.txt) | Exception Handling, Custom Errors, Debugging |
| **Day 11** | [`day11.txt`](day11.txt) | File I/O, Context Managers, Working with Text/CSV |
| **Day 12** | [`day-12.txt`](day-12.txt) | Modules, Packages, Standard Libraries |
| **Day 13** | [`day13.txt`](day13.txt) | Functional Programming, Lambdas, Map, Filter, Reduce |
| **Day 14** | [`day14.txt`](day14.txt) | Iterators, Generators, Decorators |
| **Day 15** | [`day15.txt`](day15.txt) | Regular Expressions (Regex) & Pattern Matching |
| **Day 16** | [`day16.txt`](day16.txt) | Database Concepts, SQL Basics & Table Modeling |
| **Day 17** | [`day17.txt`](day17.txt) | Relational SQL — Joins, Group By, Aggregations |
| **Day 18** | [`day18.txt`](day18.txt) | Advanced SQL — Subqueries, Indexes, Views |
| **Day 19** | [`day19.txt`](day19.txt) | Python Database Connectivity (DB-API, SQLite, MySQL) |
| **Day 20** | [`day20.txt`](day20.txt) | Full-Stack Integration, APIs & Capstone Architecture |

---

## 👥 Author & Details

- **GitHub Profile:** [@kvijaykumarr03-del](https://github.com/kvijaykumarr03-del)
- **Repository:** [Python-Full-stack-CGN](https://github.com/kvijaykumarr03-del/Python-Full-stack-CGN)

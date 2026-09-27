import streamlit as st
from grocery import Grocery_Planner

# Page configuration
st.set_page_config(
    page_title="SMART GROCERY BUDGET PLANNER",
    page_icon="🛒",
    layout="wide")
st.markdown(
    "<h1 style='text-align: center;'>🛒 SMART GROCERY BUDGET PLANNER</h1>",
    unsafe_allow_html=True)
st.markdown(
    "<p style='text-align: center;'>Plan your groceries, track expenses, and manage your monthly budget.</p>",
    unsafe_allow_html=True)

# Create planner only once
if "planner" not in st.session_state:
    st.session_state.planner = Grocery_Planner(1000)
    st.session_state.planner.load_data()
planner = st.session_state.planner

# -------------------------
# Monthly Budget
# -------------------------

st.subheader("💰 MONTHLY BUDGET")
col1, col2 = st.columns([3, 1])
with col1:
    budget = st.number_input(
        "Enter your monthly grocery budget",
        min_value=1,
        step=100,
        value=int(planner.budget))
with col2:
    st.write("")
    st.write("")
    save_budget = st.button("Save Budget")
if save_budget:
    planner.budget = budget
    planner.save_data()
    st.success("Budget saved successfully!")

# -------------------------
# Add Grocery Item
# -------------------------

st.subheader("🛍️ ADD GROCERY ITEM")
col1, col2, col3, col4 = st.columns(4)
with col1:
    name = st.text_input("Item Name")
with col2:
    category = st.selectbox(
        "Category",
        ["Food", "Dairy", "Snacks", "Beverages", "Personal Care"])
with col3:
    price = st.number_input(
        "Price",
        min_value=1,
        step=10)
with col4:
    priority = st.selectbox(
        "Priority",
        ["Essential", "Optional"])

# -------------------------
# Add Item Button
# -------------------------

if st.button("Add Item"):
    if name.strip() == "":
        st.error("Item name cannot be empty.")
    else:
        planner.add_item(
            name,
            category,
            price,
            priority)
        planner.save_data()
        st.success(f"{name} added successfully!")


st.subheader("📦 GROCERY ITEMS")
if len(planner.items) > 0:
    grocery_data = []
    for item in planner.items:
        grocery_data.append({
            "Name": item.name,
            "Category": item.category,
            "Price": item.price,
            "Priority": item.priority})
    st.table(grocery_data)
else:
    st.info("No grocery items added yet.")

# -------------------------
# Total Expense
# -------------------------

st.subheader("📊 EXPENSE SUMMARY")
total = planner.calculate_total()
col1, col2, col3 = st.columns(3)
col1.metric("💰 Monthly Budget", f"₹{planner.budget}")
col2.metric("🛒 Total Expense", f"₹{total}")
col3.metric("💵 Remaining", f"₹{planner.budget - total}")

# -------------------------
# Budget Status
# -------------------------

st.subheader("🎯 BUDGET STATUS")
if total > planner.budget:
    st.error("Budget exceeded!")
    st.write("Exceeded by:", total - planner.budget)
else:
    st.success("Within budget!")
    st.write("Remaining budget:", planner.budget - total)

# -------------------------
# Category-wise Expense
# -------------------------

st.subheader("🗂️ CATEGORY-WISE EXPENSE")
category_total = planner.Category_Summary()
if len(category_total) > 0:
    category_data = []
    for category, amount in category_total.items():
        category_data.append({
            "Category": category,
            "Amount": f"₹{amount}"})
    st.table(category_data)
else:
    st.info("No category expenses available.")

# -------------------------
# Budget Suggestions
# -------------------------

st.subheader("💡 BUDGET SUGGESTIONS")
if total > planner.budget:
    st.write("Your budget has been exceeded.")
    st.write("Consider removing some optional items:")

    for item in planner.items:
        if item.priority == "Optional":
            st.write(item.name, ":", item.price)
else:
    st.success("No suggestions needed. You are within your budget.")

# -------------------------
# Update Grocery Item
# -------------------------

st.subheader("✏️ UPDATE GROCERY ITEM")
item_names = [item.name for item in planner.items]
if len(item_names) > 0:
    col1, col2 = st.columns(2)
    with col1:
        selected_item = st.selectbox(
            "Select an item",
            item_names)
    with col2:
        new_price = st.number_input(
            "Enter new price",
            min_value=1,
            step=10)
    if st.button("Update Price"):
        for item in planner.items:
            if item.name == selected_item:
                item.price = new_price
                planner.save_data()
                st.success("Price updated successfully!")
                break
else:
    st.info("No grocery items available to update.")

# -------------------------
# Remove Grocery Item
# -------------------------

st.subheader("🗑️ REMOVE GROCERY ITEM")

item_names = [item.name for item in planner.items]

if len(item_names) > 0:

    selected_item = st.selectbox(
        "Select an item to remove",
        item_names
    )

    if st.button("Remove Item"):
        planner.remove_items(selected_item)
        st.success(f"{selected_item} removed successfully!")

else:
    st.info("No grocery items available to remove.")


public class Expense {

    public enum Category {
	BILLS, FOOD, TRANSPORTATION, ENTERTAINMENT, MISC
    }

    public String name;
    public Category category;
    public float amount;
    public String date;
    
    public Expense(String name, Category category, float amount, String date) {
	this.name = name;
	this.category = category;
	this.amount = amount;
	this.date = date;
    }
}

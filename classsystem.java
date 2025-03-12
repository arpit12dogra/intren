/**
 * A simple class system demonstration in Java
 * This class shows basic structure and components
 */
public class ClassSystem {
    // Instance variables (attributes)
    private String systemName;
    private int systemId;
    private boolean isActive;

    /**
     * Default constructor
     */
    public ClassSystem() {
        this.systemName = "Default System";
        this.systemId = 0;
        this.isActive = false;
    }

    /**
     * Parameterized constructor
     * @param systemName name of the system
     * @param systemId unique identifier for the system
     */
    public ClassSystem(String systemName, int systemId) {
        this.systemName = systemName;
        this.systemId = systemId;
        this.isActive = true;
    }

    // Getter methods
    public String getSystemName() {
        return systemName;
    }

    public int getSystemId() {
        return systemId;
    }

    public boolean isActive() {
        return isActive;
    }

    // Setter methods
    public void setSystemName(String systemName) {
        this.systemName = systemName;
    }

    public void setSystemId(int systemId) {
        if (systemId < 0) {
            throw new IllegalArgumentException("System ID cannot be negative");
        }
        this.systemId = systemId;
    }

    public void setActive(boolean active) {
        isActive = active;
    }

    /**
     * Main method to demonstrate the class usage
     * @param args command line arguments
     */
    public static void main(String[] args) {
        // Creating objects of ClassSystem
        ClassSystem sys1 = new ClassSystem();
        ClassSystem sys2 = new ClassSystem("Production System", 101);

        // Using the objects
        System.out.println("System 1 Name: " + sys1.getSystemName());
        System.out.println("System 2 Name: " + sys2.getSystemName());
    }
}
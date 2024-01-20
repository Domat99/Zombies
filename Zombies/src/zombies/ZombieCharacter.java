package zombiesgame.Zombies.src.zombies;

public class ZombieCharacter {
    public String type;
    public int health;
    public int speed;

    public ZombieCharacter (String type, int health, int speed) {
        this.health = health;
        this.type = type;
        this.speed = speed;
    }

    public void setType(String type) {
        this.type = type;
    }

    public String getType() {
        return type;
    }

    public void setHealth(int health) {
        this.health = health;
    }

    public int getHealth() {
        return health;
    }

    public void setSpeed(int speed) {
        this.speed = speed;
    }

    public int getSpeed() {
        return speed;
    }
}

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.*;
import static org.junit.Assert.assertArrayEquals;

public class MathTest {

    private Math math;

    @Before
    public void setMath(){
        math = new Math();
        System.out.println("Before");
    }

    @After
    public void tearMath(){
        math = null;
        System.out.println("After");
    }

    @Test
    public void sumChar01() {
        int result = math.sumChar(' ', ' ');
        assertEquals(64, result);
        System.out.println("Test sumChar01");
    }

    @Test
    public void sumChar02() {
        int result = math.sumChar('A', 'a');
        assertEquals(162, result);
        System.out.println("Test sumChar02");
    }

    @Test
    public void subChar01() {
        int result = math.subChar(' ', ' ');
        assertEquals(0, result);
        System.out.println("Test subChar01");
    }

    @Test
    public void subChar02() {
        int result = math.subChar('+', '-');
        assertEquals(-2, result);
        System.out.println("Test subChar02");
    }

    @Test
    public void charComparison01() {
        boolean result = math.charComparison('D', 'D');
        assertFalse(result);
        System.out.println("Test charComparison01");
    }

    @Test
    public void charComparison02() {
        boolean result = math.charComparison('F', 'Z');
        assertTrue(result);
        System.out.println("Test charComparison02");
    }

    @Test
    public void divideInt01() {
        int result = math.divideInt(1, 2);
        assertEquals(0, result);
        System.out.println("Test divideInt01");
    }

    @Test
    public void divideInt02() {
        int result = math.divideInt(4, 2);
        assertEquals(2, result);
        System.out.println("Test divideInt02");
    }

    @Test
    public void divideInt03() {
        int result = math.divideInt(0, 1);
        assertEquals(0, result);
        System.out.println("Test divideInt03");
    }

    @Test
    public void divideInt04() {
        int result = math.divideInt(4, 4);
        assertEquals(1, result);
        System.out.println("Test divideInt04");
    }

    @Test
    public void compareLengthOfStrings01() {
        boolean result = math.compareLengthOfStrings("short", "very long");
        assertFalse(result);
        System.out.println("Test compareLengthOfStrings01");
    }

    @Test
    public void compareLengthOfStrings02() {
        boolean result = math.compareLengthOfStrings("automatic testing", "this is TAU");
        assertTrue(result);
        System.out.println("Test compareLengthOfStrings02");
    }

    @Test
    public void getStringLengthDifference01() {
        int result = math.getStringLengthDifference("this isn't a test", "this is a test");
        assertEquals(3, result);
        System.out.println("Test getStringLengthDifference01");
    }

    @Test
    public void getStringLengthDifference02() {
        int result = math.getStringLengthDifference("hello","world");
        assertEquals(0, result);
        System.out.println("Test getStringLengthDifference02");
    }

    @Test
    public void isPrimeNumber01() {
        boolean status = math.primeNumber(7);
        assertTrue(status);
        System.out.println("Test isPrimeNumber01");
    }

    @Test
    public void isPrimeNumber02() {
        boolean status = math.primeNumber(13);
        assertTrue(status);
        System.out.println("Test isPrimeNumber02");
    }

}
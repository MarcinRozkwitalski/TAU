import org.junit.Test;

import static org.junit.Assert.*;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;

public class CityTest {

    @Test
    public void name(){
        City city = mock(City.class);
        when(city.name()).thenReturn("Sopot");
        String name = city.name();
        assertEquals("Sopot", name);
    }

    @Test
    public void number(){
        City city = mock(City.class);
        when(city.number()).thenReturn(42.24);
        double number = city.number();
        assertEquals(42.24, number, 1);
    }

    @Test
    public void symbol(){
        City city = mock(City.class);
        when(city.symbol()).thenReturn('~');
        char symbol = city.symbol();
        assertEquals('~', symbol);
    }

}

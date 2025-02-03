namespace san.Models
{
    public class Persona
    {
        public string Nombre{ get; set; }
        public int Edad{ get; set; }

        public Persona(string nombre, int edad)
        {
            Nombre = nombre;
            Edad = edad;
        }

        public void Saludar(){
            Console.WriteLine("Hola, mi nombre es " + Nombre + " y tengo " + Edad + " años");
        }
    }
}
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LibraryManagementSystemData
{
    public class Book
    {
        public string Name { get; set; }

        public string ISBN { get; set; }

        public Author Author { get; set; }

        public bool IsBorrowed { get; private set; } = false;

        public void BorrowBook()
        {
            if(!IsBorrowed)
                IsBorrowed = true;
        }

        public override string ToString()
        {
            string status = IsBorrowed ? "Esta Prestado" : "Esta Disponible";

            return $"Libro: {Name} Autor: {Author.Name} ISBN: {ISBN} Status: {status}";
        }
    }
}

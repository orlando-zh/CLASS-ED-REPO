using DataAccessLayer.DbConnection;
using Microsoft.Data.SqlClient;
using System;
using System.Collections.Generic;
using System.Data;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DataAccessLayer.Repositories
{
    public class DoctorRepository
    {
        private SqlDataAccess _dbConnection;

        public DoctorRepository()
        {
            _dbConnection = new SqlDataAccess();
        }

        public DataTable GetDoctors()
        {
            DataTable doctorsTable = new DataTable();

            using (var connection = _dbConnection.GetConnection())
            {
                string query = "SELECT Id, FirstName, LastName FROM Doctor";

                SqlCommand command = new SqlCommand(query, connection);
                connection.Open();

                SqlDataReader reader = command.ExecuteReader();
                doctorsTable.Load(reader);
            }

            return doctorsTable;
        }
    }
}

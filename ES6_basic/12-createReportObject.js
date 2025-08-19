export default function createReportObject(employeesList) {
  return {
    // clone the received object
    allEmployees: { ...employeesList },

    //  method ES6 (method shorthand)
    getNumberOfDepartments() {
      return Object.keys(this.allEmployees).length;
    },
  };
}

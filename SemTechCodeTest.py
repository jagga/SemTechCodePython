import unittest
import SemTechCodePython
 
class  PopulationMainTest(unittest.TestCase):

    lineStrmObj =  SemTechCodePython.LineStreamProc()
    lines = lineStrmObj.fileLines("population_2019.csv")
    Mgroups, MminPop, MmaxPop, MsumPop = lineStrmObj.getPopulationByDept(lines)

    def test_totalPopulationByDepartment(self):
        lineStrmObj =  SemTechCodePython.LineStreamProc()
        lines = lineStrmObj.fileLines("population_2019.csv")
        Mgroups, MminPop, MmaxPop, MsumPop = lineStrmObj.getPopulationByDept(lines)

        lines = self.lineStrmObj.fileLines("totpopbydept.csv")
        Tgroups, TminPop, TmaxPop, TsumPop = lineStrmObj.getPopulationByDept(lines)

        self.assertEqual(MsumPop.get("MANCHE").p, TsumPop.get("MANCHE").p)
        self.assertEqual(MsumPop.get("GIRONDE").p, TsumPop.get("GIRONDE").p)
        self.assertEqual(MsumPop.get("COTE-D'OR").p, TsumPop.get("COTE-D'OR").p)
        self.assertEqual(MsumPop.get("COTES-D'ARMOR").p, TsumPop.get("COTES-D'ARMOR").p)
        self.assertNotEqual(MsumPop.get("CALVADOS").p, TsumPop.get("CALVADOS").p)
        self.assertNotEqual(MsumPop.get("CANTAL"), TsumPop.get("CANTAL"))
        self.assertNotEqual(MsumPop.get("CHARENTE"), TsumPop.get("CHARENTE"))
        self.assertNotEqual(MsumPop.get("CHARENTE-MARITIME"), TsumPop.get("CHARENTE-MARITIME"))


    def test_maxPopulationByDepartment(self):
        lineStrmObj =  SemTechCodePython.LineStreamProc()
        lines = lineStrmObj.fileLines("population_2019.csv")
        Mgroups, MminPop, MmaxPop, MsumPop = lineStrmObj.getPopulationByDept(lines)

        self.lines =  self.lineStrmObj.fileLines("maxpopbydept.csv")
        Tgroups, TminPop, TmaxPop, TsumPop = lineStrmObj.getPopulationByDept(lines)

        self.lines = self.lineStrmObj.fileLines("maxpopbydept.csv")
        self.maxPopByDeptT = self.lineStrmObj.getPopulationByDept(lines)

        self.assertEqual(MmaxPop.get("MANCHE").p, TmaxPop.get("MANCHE").p)
        self.assertEqual(MmaxPop.get("GIRONDE").p, TmaxPop.get("GIRONDE").p)
        self.assertEqual(MmaxPop.get("COTE-D'OR").p, TmaxPop.get("COTE-D'OR").p)
        self.assertEqual(MmaxPop.get("COTES-D'ARMOR").p, TmaxPop.get("COTES-D'ARMOR").p)


    def test_minPopulationByAllDepartments(self):
        lineStrmObj =  SemTechCodePython.LineStreamProc()
        lines = lineStrmObj.fileLines("population_2019.csv")
        Mgroups, MminPop, MmaxPop, MsumPop = lineStrmObj.getPopulationByDept(lines)

        self.lines =  self.lineStrmObj.fileLines("minpopbyalldept.csv")
        Tgroups, TminPop, TmaxPop, TsumPop = lineStrmObj.getPopulationByDept(lines)


        minCities = min(MminPop.keys());
        minCitiesT = min(TminPop.keys());
        print(minCities, minCitiesT)
        self.assertEqual(minCities, minCitiesT)


if __name__ == '__main__':
    unittest.main()


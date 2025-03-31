import unittest
import SemTechCodePython
 
class  PopulationMainTest(unittest.TestCase):

    def getPopulationDetails(self):
        self.lineStrmObj =  SemTechCodePython.LineStreamProc()
        lines = self.lineStrmObj.fileLines("population_2019.csv")
        mgroups, mminpop, mmaxpop, msumpop = self.lineStrmObj.getPopulationByDept(lines)
        return mgroups, mminpop, mmaxpop, msumpop

    def test_totalPopulationByDepartment(self):
        mgroups, mminpop, mmaxpop, msumpop = self.getPopulationDetails()
        lines = self.lineStrmObj.fileLines("totpopbydept.csv")
        tgroups, tminpop, tmaxpop, tsumpop = self.lineStrmObj.getPopulationByDept(lines)
        self.assertEqual(msumpop.get("MANCHE").p, tsumpop.get("MANCHE").p)
        self.assertEqual(msumpop.get("GIRONDE").p, tsumpop.get("GIRONDE").p)
        self.assertEqual(msumpop.get("COTE-D'OR").p, tsumpop.get("COTE-D'OR").p)
        self.assertEqual(msumpop.get("COTES-D'ARMOR").p, tsumpop.get("COTES-D'ARMOR").p)
        self.assertNotEqual(msumpop.get("CALVADOS").p, tsumpop.get("CALVADOS").p)
        self.assertNotEqual(msumpop.get("CANTAL"), tsumpop.get("CANTAL"))
        self.assertNotEqual(msumpop.get("CHARENTE"), tsumpop.get("CHARENTE"))
        self.assertNotEqual(msumpop.get("CHARENTE-MARITIME"), tsumpop.get("CHARENTE-MARITIME"))


    def test_maxPopulationByDepartment(self):
        mgroups, mminpop, mmaxpop, msumpop = self.getPopulationDetails()
        lines =  self.lineStrmObj.fileLines("maxpopbydept.csv")
        tgroups, tminpop, tmaxpop, tsumpop = self.lineStrmObj.getPopulationByDept(lines)
        self.assertEqual(mmaxpop.get("MANCHE").p, tmaxpop.get("MANCHE").p)
        self.assertEqual(mmaxpop.get("GIRONDE").p, tmaxpop.get("GIRONDE").p)
        self.assertEqual(mmaxpop.get("COTE-D'OR").p, tmaxpop.get("COTE-D'OR").p)
        self.assertEqual(mmaxpop.get("COTES-D'ARMOR").p, tmaxpop.get("COTES-D'ARMOR").p)


    def test_minPopulationByAllDepartments(self):
        mgroups, mminpop, mmaxpop, msumpop = self.getPopulationDetails()
        lines =  self.lineStrmObj.fileLines("minpopbyalldept.csv")
        tgroups, tminpop, tmaxpop, tsumpop = self.lineStrmObj.getPopulationByDept(lines)
        mincities = min(mminpop.keys())
        mincitiest = min(tminpop.keys())
        print(mincities, mincitiest)
        self.assertEqual(mincities, mincitiest)


if __name__ == '__main__':
    unittest.main()


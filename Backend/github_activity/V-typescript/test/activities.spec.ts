import { describe, it, vi, beforeEach, expectTypeOf } from "vitest";
import { getGitUserActivity } from "../src";



describe('Testing github activities function', ()=>{
  beforeEach(() =>{
    vi.resetAllMocks()
  })

  it("should return list of objects", async () => {
    const result = await getGitUserActivity("user");

    expectTypeOf(result).toBeArray
  });
})
----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date: 27.08.2024 17:16:45
-- Design Name: 
-- Module Name: timer - Behavioral
-- Project Name: 
-- Target Devices: 
-- Tool Versions: 
-- Description: 
-- 
-- Dependencies: 
-- 
-- Revision:
-- Revision 0.01 - File Created
-- Additional Comments:
-- 
----------------------------------------------------------------------------------

library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_ARITH.ALL;
use IEEE.STD_LOGIC_UNSIGNED.ALL;


entity Timing_block is
    Port (
        clk_in : in STD_LOGIC; -- 100 MHz input clock
        mux_select : out STD_LOGIC_VECTOR (1 downto 0); -- Signal for the mux
        anodes : out STD_LOGIC_VECTOR (3 downto 0) -- Anodes signal for display
    );
end Timing_block;

architecture Behavioral of Timing_block is
    constant N : integer := 50000;-- <need to select correct value>
    signal counter: integer := 0;
    signal new_clk : STD_LOGIC := '1';
    signal mux_inp : STD_LOGIC_VECTOR (1 downto 0) := "00";
begin
    --Process 1 for dividing the clock from 100 Mhz to 1Khz - 60hz
    NEW_CLOCK: process(clk_in)
    begin
        if rising_edge(clk_in) then
            counter <= counter + 1;
            if counter > N/2 then
                new_clk <= not new_clk;
                counter <= 0;
            end if;
        end if;
    end process;
    --Process 2 for mux select signal
    MUX_sel_proc: process(new_clk)
    begin
        if rising_edge(new_clk) then
            mux_inp <= mux_inp + 1;
        end if;
        mux_select <= mux_inp;
    end process;
    --Process 3 for anode signal
    ANODE_sel: process(mux_inp)
    begin
        if mux_inp = "00" then
            anodes <= "1110";
        elsif mux_inp = "01" then
            anodes <= "1101";
        elsif mux_inp = "10" then
            anodes <= "1011";
        else
            anodes <= "0111";

        end if;
    end process;
end Behavioral;
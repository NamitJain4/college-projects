----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date: 03.09.2024 16:21:27
-- Design Name: 
-- Module Name: main_tb - Behavioral
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

-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--use IEEE.NUMERIC_STD.ALL;

-- Uncomment the following library declaration if instantiating
-- any Xilinx leaf cells in this code.
--library UNISIM;
--use UNISIM.VComponents.all;

entity main_tb is
end main_tb;

architecture tb of main_tb is
    component project4_digital
        Port (
            clk_in : in STD_LOGIC;
            s1 : in STD_LOGIC;
            s2 : in STD_LOGIC;
            s3 : in STD_LOGIC;
            s4 : in STD_LOGIC;
            s5 : in STD_LOGIC;
            s6 : in STD_LOGIC;
            s7 : in STD_LOGIC;
            s8 : in STD_LOGIC;
            s9 : in STD_LOGIC;
            s10 : in STD_LOGIC;
            s11 : in STD_LOGIC;
            s12 : in STD_LOGIC;
            s13 : in STD_LOGIC;
            s14 : in STD_LOGIC;
            s15 : in STD_LOGIC;
            s16 : in STD_LOGIC;
            c1 : out STD_LOGIC;
            c2 : out STD_LOGIC;
            c3 : out STD_LOGIC;
            c4 : out STD_LOGIC;
            c5 : out STD_LOGIC;
            c6 : out STD_LOGIC;
            c7 : out STD_LOGIC;
            anode_sel : out STD_LOGIC_VECTOR
        );
    end component;
    signal s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16, c1, c2, c3, c4, c5, c6, c7, a1, a2, a3, a4 : STD_LOGIC;
    signal clk_in : std_logic := '0';
begin
    UUT : project4_digital port map (clk_in => clk_in, s1 => s1, s2 => s2, s3 => s3, s4 => s4, s5 => s5, s6 => s6, s7 => s7, s8 => s8, s9 => s9, s10 => s10, s11 => s11, s12 => s12, s13 => s13, s14 => s14, s15 => s15, s16 => s16, c1 => c1, c2 => c2, c3 => c3, c4 => c4, c5 => c5, c6 => c6, c7 => c7, anode_sel(0) => a1, anode_sel(1) => a2, anode_sel(2) => a3, anode_sel(3) => a4);
    change_clk: process
    begin
        wait for 5 ns;
        clk_in <= not clk_in;
    end process;
    s1 <= '0';
    s2 <= '0';
    s3 <= '0';
    s4 <= '1';
    s5 <= '0';
    s6 <= '0';
    s7 <= '1';
    s8 <= '0';
    s9 <= '0';
    s10 <= '0';
    s11 <= '1';
    s12 <= '1';
    s13 <= '0';
    s14 <= '1';
    s15 <= '0';
    s16 <= '0';
end tb;
